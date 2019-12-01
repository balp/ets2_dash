#!/usr/bin/env python3
#
# Run GUI with mock data.

import PySimpleGUI
import json

from ets2_dash.model import Model
from ets2_dash.view import View


def setup():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    with open("data/info.json", "r") as j:
        model.set_info(json.load(j))
    with open("data/game.json", "r") as j:
        model.set_game(json.load(j))
    with open("data/job.json", "r") as j:
        model.set_job_config(json.load(j))
    with open("data/truck_config.json", "r") as j:
        model.set_truck_config(json.load(j))
    with open("data/trailer_config.json", "r") as j:
        model.set_trailer_config(json.load(j))
    return model


def main(data_values):
    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(data_values)

    _, _ = hmi.window.Read(timeout=100)

    hmi.update_data()

    event, values = hmi.window.Read()
    print("Event: ", event)
    print("Values: ", values)


if __name__ == '__main__':
    main(setup())
