#!/usr/bin/env python3
import PySimpleGUI

from ets2.mqtt_handler import mqtt_model_handler, mqtt_event_loop
from ets2_dash.view import View


def main():
    model, mqtt_reader_thread, state, work_log = mqtt_model_handler()
    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(model)
    mqtt_event_loop(hmi, mqtt_reader_thread, state)


if __name__ == '__main__':
    main()
