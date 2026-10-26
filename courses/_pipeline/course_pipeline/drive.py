"""Read-only Google Drive transport using an existing rclone OAuth configuration.

No credential is logged or embedded in artifacts. Range downloads resume locally.
"""
from __future__ import annotations

import configparser
import json
import os
import time
from pathlib import Path
import requests
from .common import digest, write_json


class Drive:
    def __init__(self, config_path=None, remote="bili_drive", credentials=None):
        self.config_path = config_path
        self.remote = remote
        self.credentials = credentials
        self.http = requests.Session()
        self.token = None
        self.expires = 0

    def _auth(self):
        if self.credentials is not None:
            from google.auth.transport.requests import Request
            if not self.credentials.valid:
                self.credentials.refresh(Request())
            return self.credentials.token
        if self.token and time.time() < self.expires:
            return self.token
        config = configparser.ConfigParser(interpolation=None)
        if not config.read(self.config_path):
            raise RuntimeError("rclone configuration unavailable")
        c = config[self.remote]
        stored = json.loads(c["token"])
        if not c.get("client_id") or not c.get("client_secret"):
            raise RuntimeError("Use a custom OAuth rclone client or Google ADC; built-in rclone client is not embedded")
        res = self.http.post("https://oauth2.googleapis.com/token", data={
            "client_id": c["client_id"], "client_secret": c["client_secret"],
            "refresh_token": stored["refresh_token"], "grant_type": "refresh_token"}, timeout=45)
        if res.status_code != 200:
            raise RuntimeError(f"Drive token refresh failed (HTTP {res.status_code})")
        data = res.json()
        self.token = data["access_token"]
        self.expires = time.time() + data.get("expires_in", 3600) - 90
        return self.token

    def get(self, suffix, **kwargs):
        for attempt in range(5):
            headers = dict(kwargs.pop("headers", {})) if attempt == 0 else headers
            headers["Authorization"] = "Bearer " + self._auth()
            r = self.http.get("https://www.googleapis.com/drive/v3/" + suffix,
                              headers=headers, timeout=(20, 120), **kwargs)
            if r.status_code == 401:
                r.close()
                self.expires = 0
                continue
            if r.status_code in (429, 500, 502, 503, 504):
                r.close()
                time.sleep(min(2 ** attempt, 16))
                continue
            if r.status_code not in (200, 206):
                status = r.status_code
                r.close()
                raise RuntimeError(f"Drive read failed (HTTP {status})")
            return r
        raise RuntimeError("Drive retry limit reached")

    def metadata(self, file_id):
        return self.get("files/" + file_id, params={"supportsAllDrives": "true", "fields":
            "id,name,size,md5Checksum,sha256Checksum,modifiedTime,version,mimeType,parents,videoMediaMetadata"}).json()

    def list_folder(self, folder_id):
        token = None
        while True:
            params = {"q": f"'{folder_id}' in parents and trashed = false", "pageSize": 1000,
                      "supportsAllDrives": "true", "includeItemsFromAllDrives": "true",
                      "fields": "nextPageToken,files(id,name,mimeType,size,md5Checksum,sha256Checksum,videoMediaMetadata)"}
            if token:
                params["pageToken"] = token
            d = self.get("files", params=params).json()
            yield from d.get("files", [])
            token = d.get("nextPageToken")
            if not token:
                break

    def download(self, file_id, destination):
        dest = Path(destination)
        dest.parent.mkdir(parents=True, exist_ok=True)
        meta = self.metadata(file_id)
        expected_size = int(meta["size"])
        expected_md5 = meta.get("md5Checksum")
        if dest.exists() and dest.stat().st_size == expected_size and (
                not expected_md5 or digest(dest, "md5") == expected_md5):
            return {**meta, "local_sha256": digest(dest), "reused": True}
        part = dest.with_suffix(dest.suffix + ".part")
        marker = part.with_suffix(part.suffix + ".source.json")
        identity = {k: meta.get(k) for k in ("id", "size", "md5Checksum", "version", "modifiedTime")}
        if part.exists() and (not marker.exists() or json.loads(marker.read_text()) != identity):
            part.unlink()  # Only our invalid local partial; never the Drive source.
        write_json(marker, identity)
        for attempt in range(5):
            offset = part.stat().st_size if part.exists() else 0
            if offset > expected_size:
                part.unlink()
                offset = 0
            if offset == expected_size:
                break
            try:
                headers = {"Range": f"bytes={offset}-"} if offset else {}
                with self.get("files/" + file_id, params={"alt": "media", "supportsAllDrives": "true"},
                              headers=headers, stream=True) as res:
                    if offset and res.status_code == 200:
                        offset = 0  # Provider ignored Range; safely restart, never append full content.
                    if res.status_code == 206 and not res.headers.get("Content-Range", "").startswith(f"bytes {offset}-"):
                        raise RuntimeError("Wrong Content-Range")
                    with part.open("ab" if offset else "wb") as out:
                        for block in res.iter_content(4 * 1024 * 1024):
                            if block:
                                out.write(block)
                        out.flush()
                        os.fsync(out.fileno())
                if part.stat().st_size == expected_size:
                    break
            except (requests.RequestException, OSError):
                if attempt == 4:
                    raise
            time.sleep(2 ** attempt)
        if not part.exists() or part.stat().st_size != expected_size:
            raise RuntimeError("Incomplete Drive download")
        if expected_md5 and digest(part, "md5") != expected_md5:
            part.unlink()
            raise RuntimeError("Drive MD5 checksum mismatch; invalid local partial removed")
        sha = digest(part)
        if meta.get("sha256Checksum") and sha != meta["sha256Checksum"]:
            raise RuntimeError("Drive SHA256 checksum mismatch")
        part.replace(dest)
        marker.unlink(missing_ok=True)
        return {**meta, "local_sha256": sha, "reused": False}
