from test.utils import rerun_data_from_files


def test_save_job():
    _, work_log = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2"],
                                        'test_save_job')
