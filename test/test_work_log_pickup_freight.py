import bz2
import json

import jsonpickle as jsonpickle
from approvaltests import verify_with_namer, get_default_reporter
from approvaltests.core.namer import Namer

from ets2.model import Model, add_json_to_model
from ets2_worklog.model import WorkLog, add_json_to_work_log


def test_pickup_freight():
    work_log = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2"])

    verify_work_log_as_json(work_log)


def test_deliver_freight():
    work_log = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                      "data/ats_end_port_ang_coos_bay.mqtt.json.bz2"])
    verify_work_log_as_json(work_log)


def test_2_freights():
    work_log = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                      "data/ats_end_port_ang_coos_bay.mqtt.json.bz2",
                                      "data/ats_start_coos_dalles_short.mqtt.json.bz2",
                                      "data/ats_end_coos_dalles_short.mqtt.json.bz2"
                                      ])
    verify_work_log_as_json(work_log)


def verify_work_log_as_json(work_log):
    jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    jsonpickle.set_preferred_backend('json')
    verify_with_namer(data=jsonpickle.encode(work_log),
                      namer=Namer(extension='.json'),
                      reporter=get_default_reporter())


def rerun_data_from_files(files):
    model = Model()
    work_log: WorkLog = WorkLog(model)
    for f in files:
        with bz2.open(f) as gj:
            for line in gj:
                topic, json_str = line.decode('utf8').split(" ", 1)
                json_data = json.loads(json_str)
                add_json_to_model(model, json_data, topic)
                add_json_to_work_log(work_log, json_data, topic)
    return work_log
