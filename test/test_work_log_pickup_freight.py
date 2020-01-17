from test.utils import rerun_data_from_files, verify_work_log_as_json


def test_pickup_freight():
    _, work_log, _ = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2"],
                                           'test_pickup_freight')

    verify_work_log_as_json(work_log)


def test_deliver_freight():
    _, work_log, _ = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_end_port_ang_coos_bay.mqtt.json.bz2"],
                                           'test_deliver_freight')
    verify_work_log_as_json(work_log)


def test_2_freights():
    _, work_log, _ = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_end_port_ang_coos_bay.mqtt.json.bz2",
                                            "data/ats_start_coos_dalles_short.mqtt.json.bz2",
                                            "data/ats_end_coos_dalles_short.mqtt.json.bz2"
                                            ], 'test_2_freights')
    verify_work_log_as_json(work_log)


