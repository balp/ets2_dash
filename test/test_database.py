from approvaltests import verify

from ets2.model import Model
from ets2.work_log import WorkLog
from test.utils import rerun_data_from_files, verify_work_log_as_json


def test_save_job():
    _, _, database = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2"],
                                           'test_save_job')
    lines = []
    for line in database._conn.iterdump():
        lines.append(line)
    verify('\n'.join(lines))


def test_generate_object_from():
    _, _, database = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2"],
                                           'test_save_job')
    model = Model()
    work_log = WorkLog(model, database)

    verify_work_log_as_json(work_log)


def test_save_2_freights():
    _, _, database = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_end_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_start_coos_dalles_short.mqtt.json.bz2",
                                            "data/ats_end_coos_dalles_short.mqtt.json.bz2"
                                            ], 'test_2_freights')
    lines = []
    for line in database._conn.iterdump():
        lines.append(line)
    verify('\n'.join(lines))


def test_load_2_freights():
    _, _, database = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_end_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_start_coos_dalles_short.mqtt.json.bz2",
                                            "data/ats_end_coos_dalles_short.mqtt.json.bz2"
                                            ], 'test_2_freights')
    model = Model()
    work_log = WorkLog(model, database)
    verify_work_log_as_json(work_log)