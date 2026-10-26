import hashlib
import requests
import pytest
from course_pipeline.drive import Drive
from course_pipeline.common import write_json


class Response:
    def __init__(self,data,status,headers=None):
        self.data=data;self.status_code=status;self.headers=headers or {}
    def __enter__(self):return self
    def __exit__(self,*args):pass
    def iter_content(self,size):yield self.data


class FakeDrive(Drive):
    def __init__(self,data,ignore_range=False):
        self.data=data;self.ignore_range=ignore_range;self.ranges=[]
    def metadata(self,id):
        return {'id':id,'size':str(len(self.data)),'md5Checksum':hashlib.md5(self.data).hexdigest(),'version':'1','modifiedTime':'t'}
    def get(self,suffix,headers,**kwargs):
        r=headers.get('Range');self.ranges.append(r)
        if r and not self.ignore_range:
            n=int(r.split('=')[1].split('-')[0]);return Response(self.data[n:],206,{'Content-Range':f'bytes {n}-{len(self.data)-1}/{len(self.data)}'})
        return Response(self.data,200)


@pytest.mark.parametrize('ignore_range',[False,True])
def test_resume_or_server_ignored_range_never_duplicates_bytes(tmp_path,ignore_range):
    d=FakeDrive(b'complete source content',ignore_range)
    dest=tmp_path/'v.mp4';partial=tmp_path/'v.mp4.part';partial.write_bytes(d.data[:7])
    write_json(tmp_path/'v.mp4.part.source.json',d.metadata('id'))
    receipt=d.download('id',dest)
    assert d.ranges==['bytes=7-']
    assert dest.read_bytes()==d.data
    assert receipt['local_sha256']==hashlib.sha256(d.data).hexdigest()


def test_changed_source_discards_only_old_partial(tmp_path):
    d=FakeDrive(b'new media');dest=tmp_path/'v.mp4';(tmp_path/'v.mp4.part').write_bytes(b'old')
    write_json(tmp_path/'v.mp4.part.source.json',{'id':'other'})
    d.download('id',dest)
    assert d.ranges==[None] and dest.read_bytes()==d.data


def test_completed_file_is_verified_before_skip(tmp_path):
    d=FakeDrive(b'source');dest=tmp_path/'v.mp4';dest.write_bytes(b'source')
    receipt=d.download('id',dest)
    assert receipt['reused'] and not d.ranges
