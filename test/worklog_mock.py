#!/usr/bin/env python3
#
# Run Worklog GUI with mock data.


import PySimpleGUI
from ets2_worklog.view import View
from test.utils import rerun_data_from_files


def setup():
    model, work_log = rerun_data_from_files(["data/ats_start_port_ang_coos_bay.mqtt.json.bz2",
                                             "data/ats_end_port_ang_coos_bay.mqtt.json.bz2",
                                             "data/ats_start_coos_dalles_short.mqtt.json.bz2",
                                             "data/ats_end_coos_dalles_short.mqtt.json.bz2"
                                             ], 'work_log_mock')

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
    _data_values, _work_log = setup()
    main(_data_values, _work_log)
