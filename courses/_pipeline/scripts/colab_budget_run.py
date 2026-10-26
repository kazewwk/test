#!/usr/bin/env python3
"""Run an explicitly budget-authorized Colab task and always release its session.

No purchases or top-ups. Pass --approved-units only after user authorization.
The deadline includes allocation, setup, download and processing. The runtime's
reported rate determines an earlier stop; billing precision/latency is recorded.
"""
import argparse
import json
import re
import subprocess
import threading
import time
from pathlib import Path


def cli(args,timeout=90):
    r=subprocess.run(['colab',*args],capture_output=True,text=True,timeout=timeout)
    if r.returncode:
        raise RuntimeError(f'colab {args[0]} failed; exit {r.returncode}')
    return r.stdout


def usage():
    text=cli(['usage'],45)
    def value(pattern):
        m=re.search(pattern,text)
        if not m:raise ValueError('Cannot read Colab billing meter')
        return float(m[1])
    return {'balance':value(r'Current balance:\s*([0-9.]+)'),
            'rate':value(r'Usage rate:\s*([0-9.]+)'),
            'active':int(value(r'Active assignments:\s*(\d+)'))}


def main():
    p=argparse.ArgumentParser()
    p.add_argument('--session',required=True)
    p.add_argument('--accelerator',choices=['cpu','T4','L4'],required=True)
    p.add_argument('--approved-units',type=float,required=True)
    p.add_argument('--max-hours',type=float,default=2)
    p.add_argument('--script',required=True,type=Path)
    p.add_argument('--upload',action='append',default=[],help='LOCAL_PATH=REMOTE_PATH')
    p.add_argument('--download',action='append',default=[],help='REMOTE_PATH=LOCAL_PATH')
    p.add_argument('--receipt',type=Path,required=True)
    a=p.parse_args()
    if a.approved_units<=0 or a.max_hours<=0 or not a.script.is_file():
        p.error('Positive budget, deadline and existing task script are required')
    before=usage()
    if before['active']:
        raise RuntimeError('Existing sessions affect account-level metering; isolate before this budgeted run')
    if before['balance']<a.approved_units:
        raise RuntimeError('Budget exceeds existing balance; this tool never purchases compute')
    receipt={'session':a.session,'accelerator':a.accelerator,'approved_units':a.approved_units,
             'before':before,'samples':[],'state':'starting','currency_cost':None}
    a.receipt.parent.mkdir(parents=True,exist_ok=True)
    def save():a.receipt.write_text(json.dumps(receipt,indent=2))
    ended=threading.Event();stopped=threading.Event();started=time.monotonic();rate=0
    def stop():
        if stopped.is_set():return
        try:
            cli(['stop','-s',a.session],60)
            receipt['released']=True;stopped.set()
        except Exception as e:
            receipt['release_error']=type(e).__name__
        save()
    def watch():
        nonlocal rate
        while not ended.wait(15):
            elapsed=(time.monotonic()-started)/3600
            try:
                meter=usage();rate=max(rate,meter['rate'])
                receipt['samples'].append({'elapsed_hours':elapsed,**meter});save()
                # Reserve at least one minute of billed time for saving and stopping.
                estimated=rate*(elapsed+1/60)
                used=before['balance']-meter['balance']
                if max(estimated,used)>=a.approved_units or elapsed>=a.max_hours:
                    receipt['state']='budget_or_deadline_stop';stop();return
            except Exception as e:
                receipt['state']='meter_unavailable_stop';receipt['meter_error']=type(e).__name__
                stop();return
    thread=None
    try:
        args=['new','-s',a.session]
        if a.accelerator!='cpu':args+=['--gpu',a.accelerator]
        cli(args,120)
        meter=usage();rate=meter['rate'];receipt['samples'].append({'elapsed_hours':(time.monotonic()-started)/3600,**meter})
        if rate/60>=a.approved_units:
            raise RuntimeError('Budget is too small for one minute at the assigned rate')
        receipt['state']='running';save()
        thread=threading.Thread(target=watch,daemon=True);thread.start()
        for mapping in a.upload:
            local,remote=mapping.split('=',1);cli(['upload','-s',a.session,local,remote],180)
        # CLI output may contain program logs; capture privately outside the repository.
        with a.receipt.with_suffix('.log').open('w') as log:
            child=subprocess.Popen(['colab','exec','-s',a.session,'--timeout',str(int(a.max_hours*3600)),
                                    '-f',str(a.script)],stdout=log,stderr=subprocess.STDOUT)
            while child.poll() is None:
                if stopped.wait(1):
                    child.terminate();child.wait(timeout=20);break
            if child.returncode:
                raise RuntimeError('Remote task failed or was stopped; inspect private log')
        for mapping in a.download:
            remote,local=mapping.split('=',1);cli(['download','-s',a.session,remote,local],180)
        receipt['state']='task_finished'
    finally:
        ended.set()
        if thread:thread.join(timeout=50)
        stop()
        receipt['elapsed_seconds']=time.monotonic()-started
        try:
            receipt['after']=usage()
            receipt['displayed_balance_difference']=before['balance']-receipt['after']['balance']
            receipt['estimated_units_from_rate']=rate*receipt['elapsed_seconds']/3600
        finally:save()


if __name__=='__main__':main()
