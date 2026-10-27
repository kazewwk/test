from course_pipeline.health import progress_signature,recovery_reason,inspect_runtime


def running():
    return {'driver_exists':True,'driver_alive':True,'driver':{'state':'running_batch'},
            'workers':{'gpu':{'alive':True},'finish':{'alive':True}},
            'batch':{'completed':1,'updated_at':'heartbeat'},
            'progress':[{'drive_file_id':'source','counts':{'document':10},'latest_artifact_mtime':50}]}


def test_heartbeat_alone_does_not_disguise_stalled_work():
    first=running();second=running();second['batch']['updated_at']='new heartbeat'
    assert progress_signature(first)==progress_signature(second)
    assert recovery_reason(second,100,2000)=='no_artifact_progress'


def test_completed_frame_advances_progress_without_finishing_lesson():
    first=running();second=running();second['progress'][0]['counts']['document']=11
    assert progress_signature(first)!=progress_signature(second)
    assert recovery_reason(second,1900,2000) is None


def test_dead_worker_is_detected_even_while_driver_survives():
    status=running();status['workers']['gpu']['alive']=False
    assert recovery_reason(status,1999,2000)=='worker_disappeared'


def test_environment_install_is_not_mistaken_for_stalled_inference():
    status=running();status['driver']['state']='environment'
    assert recovery_reason(status,0,99999) is None


def test_completed_gpu_producer_may_exit_while_api_publication_continues():
    status=running();status['workers']['gpu']['alive']=False;status['gpu_done']={'failures':[]}
    assert recovery_reason(status,1999,2000) is None


def test_empty_runtime_probe_is_safe_during_bootstrap(tmp_path):
    status=inspect_runtime(tmp_path)
    assert not status['driver_exists'] and not status['driver_alive']
    assert status['progress']==[]
