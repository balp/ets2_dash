#/usr/bin/env python3
#
# Run GUI with mock data.

import PySimpleGUI
import json

from ets2_dash.model import Model
from ets2_dash.view import View


def setup():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    return model


def main(data):
    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(data)

    event, values = hmi.window.ReadNonBlocking()

    hmi.updateData()

    event, values = hmi.window.Read()
    print("Event: ", event)
    print("Values: ", values)



if __name__ == '__main__':
    data = setup()
    main(data)

