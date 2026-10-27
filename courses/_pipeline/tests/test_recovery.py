"""Real process termination must preserve evidence and exclude unrelated processes."""
from pathlib import Path
import importlib.util,json,subprocess,sys,time
from types import SimpleNamespace


def test_recovery_terminates_only_owned_process_group_and_keeps_evidence(tmp_path,monkeypatch):
    module_path=Path(__file__).resolve().parents[1]/'scripts/runtime_driver.py'
    spec=importlib.util.spec_from_file_location('runtime_driver_recovery_test',module_path)
    module=importlib.util.module_from_spec(spec);spec.loader.exec_module(module)
    scripts=tmp_path/'pipeline/scripts';scripts.mkdir(parents=True)
    worker=scripts/'batch_concurrent.py';worker.write_text('import time\ntime.sleep(60)\n')
    unrelated=tmp_path/'unrelated.py';unrelated.write_text('import time\ntime.sleep(60)\n')
    owned=subprocess.Popen([sys.executable,str(worker)],start_new_session=True)
    other=subprocess.Popen([sys.executable,str(unrelated)],start_new_session=True)
    try:
        (tmp_path/'cache').mkdir()
        (tmp_path/'cache/batch_processes.json').write_text(json.dumps({'gpu':owned.pid,'finish':other.pid}))
        evidence=tmp_path/'evidence.json';evidence.write_text('{"verified":"keep"}')
        launches=[]
        def launch(args,**kwargs):
            launches.append((args,kwargs));return SimpleNamespace(pid=999999)
        monkeypatch.setattr(module.subprocess,'Popen',launch)
        module.recover(tmp_path,'cuda:0')
        assert owned.wait(timeout=5)<0
        assert other.poll() is None
        assert evidence.read_text()=='{"verified":"keep"}'
        assert (tmp_path/'batch_driver.pid').read_text()=='999999'
        assert '--resume-existing' in launches[0][0]
        assert launches[0][1]['start_new_session'] is True
    finally:
        if owned.poll() is None:owned.kill();owned.wait()
        if other.poll() is None:other.kill();other.wait()
