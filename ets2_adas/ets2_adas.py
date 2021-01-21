#!/usr/bin/env python3
import logging

import PySimpleGUI

from ets2.mqtt_handler import mqtt_model_handler, mqtt_event_loop
from ets2_adas.view import View


def main():
    logging.basicConfig(format='%(asctime)s %(message)s', level=logging.DEBUG)
    model, mqtt_reader_thread, state, work_log = mqtt_model_handler()
    hmi = View(model)
    mqtt_event_loop(hmi, mqtt_reader_thread, state)


if __name__ == '__main__':
    main()
