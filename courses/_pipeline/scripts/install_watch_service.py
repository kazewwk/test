#!/usr/bin/env python3
"""Install the task's persistent user service; credentials remain in private files."""
from pathlib import Path
import argparse,subprocess,sys


def main():
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--task-root',required=True)
    p.add_argument('--session',required=True)
    p.add_argument('--accelerator',choices=['L4','NONE'],default='L4')
    a=p.parse_args();root=Path(a.task_root).resolve();private=root/'private'
    args=[sys.executable,str(Path(__file__).resolve().with_name('colab_controller.py'))]
    for option,name in [('colab-state','colab_sessions.json'),('ssh-key','colab_ed25519'),
                        ('rclone-config','drive-runtime.conf'),('github-token-file','github-publisher-token'),
                        ('inventory','inventory.json'),('pilot-review','pilot_review.json'),
                        ('api-config','vision_api_credentials.json')]:
        path=private/name
        if not path.is_file():raise SystemExit('Missing private input: '+str(path))
        args.extend(['--'+option,str(path)])
    args+=['--workspace',str(private/'controller'),'--session',a.session,'--accelerator',a.accelerator,'--use-existing-balance']
    def quote(value):return '"'+str(value).replace('%','%%').replace('\\','\\\\').replace('"','\\"')+'"'
    unit=Path.home()/'.config/systemd/user/nce-course-watch.service';unit.parent.mkdir(parents=True,exist_ok=True)
    unit.write_text('[Unit]\nDescription=New Concept course processing monitor\nAfter=network-online.target\nWants=network-online.target\nStartLimitIntervalSec=0\n\n[Service]\nType=simple\nWorkingDirectory='+str(root).replace('%','%%')+'\nEnvironment='+quote('PATH='+str(Path.home()/'.local/bin')+':/usr/local/bin:/usr/bin:/bin')+'\nExecStart='+' '.join(quote(v) for v in args)+'\nRestart=on-failure\nRestartSec=10\nUMask=0077\n\n[Install]\nWantedBy=default.target\n')
    subprocess.run(['systemd-analyze','--user','verify',str(unit)],check=True)
    subprocess.run(['systemctl','--user','daemon-reload'],check=True)
    subprocess.run(['systemctl','--user','enable','--now',unit.name],check=True)
    subprocess.run(['systemctl','--user','is-active','--quiet',unit.name],check=True)
    result=subprocess.run(['systemctl','--user','show',unit.name,'-p','ActiveState','-p','SubState','-p','MainPID','-p','Restart'],capture_output=True,text=True,check=True)
    print(result.stdout,end='')


if __name__=='__main__':main()
