#!/usr/bin/env python3
#
# Run GUI with mock data.

import PySimpleGUI
import json

from ets2.model import Model
from ets2_worklog.view import View
from ets2_worklog.model import WorkLog


def setup():
    model = Model()
    work_log = WorkLog(model)
    telematic_files = ["data/telematic.json",
                       "data/telematic_1_01.json",
                       "data/telematic_breaking.json",
                       "data/telematic_engine_break.json",
                       "data/telematic_freeride.json",
                       "data/telematic_reststop.json"]
    for telematic_file in telematic_files:
        with open(telematic_file, "r") as j:
            model.set_telematic_data(json.load(j))
    with open("data/info.json", "r") as j:
        model.set_info(json.load(j))
    with open("data/game.json", "r") as j:
        model.set_game(json.load(j))
    with open("data/job.json", "r") as j:
        model.set_job_config(json.load(j))
    with open("data/truck_config.json", "r") as j:
        model.set_truck_config(json.load(j))
    with open("data/trailer_dual_0.json", "r") as j:
        model.set_trailer_config(json.load(j), 0)
    with open("data/trailer_dual_1.json", "r") as j:
        model.set_trailer_config(json.load(j), 1)
    return model, work_log


def main(data_values, work_log):
    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(data_values, work_log)

    _, _ = hmi.window.Read(timeout=100)

    hmi.update_data()

    event, values = hmi.window.Read()
    print("Event: ", event)
    print("Values: ", values)


if __name__ == '__main__':
    data_values, work_log = setup()
    main(data_values, work_log)
