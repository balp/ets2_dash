import bz2
import json

import jsonpickle as jsonpickle
import pytest
from approvaltests import verify_with_namer, get_default_reporter
from approvaltests.core.namer import Namer

from ets2.model import Model, add_json_to_model
from ets2_worklog.model import WorkLog

def test_pickup_freight():
    model = Model()
    work_log: WorkLog = WorkLog(model)

    with bz2.open("data/ats_start_port_ang_coos_bay.mqtt.json.bz2") as gj:
        for line in gj:
            topic, json_str = line.decode('utf8').split(" ", 1)
            json_data = json.loads(json_str)
            add_json_to_model(model, json_data, topic)
    jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    jsonpickle.set_preferred_backend('json')
    verify_with_namer(data=jsonpickle.encode(work_log),
                      namer=Namer(extension='.json'),
                      reporter=get_default_reporter())

def test_deliver_freight():
    model = Model()
    work_log: WorkLog = WorkLog(model)
    for f in ["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
              "data/ats_end_port_ang_coos_bay.mqtt.json.bz2"]:
        with bz2.open(f) as gj:
            for line in gj:
                topic, json_str = line.decode('utf8').split(" ", 1)
                json_data = json.loads(json_str)
                add_json_to_model(model, json_data, topic)
        jsonpickle.set_encoder_options('json', sort_keys=True, indent=4)
    jsonpickle.set_preferred_backend('json')
    verify_with_namer(data=jsonpickle.encode(work_log),
                      namer=Namer(extension='.json'),
                      reporter=get_default_reporter())



