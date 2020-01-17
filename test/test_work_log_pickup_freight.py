import jsonpickle as jsonpickle
from approvaltests import verify_with_namer, get_default_reporter
from approvaltests.core.namer import Namer

from test.utils import rerun_data_from_files


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


def verify_work_log_as_json(work_log):
    jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    jsonpickle.set_preferred_backend('json')
    verify_with_namer(data=jsonpickle.encode(work_log),
                      namer=Namer(extension='.json'),
                      reporter=get_default_reporter())
