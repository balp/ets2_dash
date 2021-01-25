import decimal
import datetime
import logging
from pathlib import Path

import PySimpleGUI
import ets2.model


def info_label(label, key):
    return [PySimpleGUI.Text(label,
                             size=(11, 1),
                             justification="left"),
            PySimpleGUI.Text("---",
                             size=(5, 1),
                             justification="right",
                             key=key)]


def format_decimal(value):
    decimal_value = decimal.Decimal(value)
    return f'{decimal_value:.3f}'


class View:
    def __init__(self, data: ets2.model.Model):
        self._data: ets2.model.Model = data
        self._data.register_observer(self)
        self._log = logging.getLogger("view")
        self._adas_ok = False
        game_info = [PySimpleGUI.Text('',
                                      size=(70, 1),
                                      justification="center",
                                      key="game_name"),
                     PySimpleGUI.Text('',
                                      size=(20, 1),
                                      justification="left",
                                      key="game_pause")
                     ]

        exit_button_layout = [
            PySimpleGUI.Exit(button_color=('white', 'firebrick4'))
        ]
        info = [
            info_label('input_steering', 'input_steering'),
            # info_label('wheel_steering', 'wheel_steering'),
            info_label('effective_steering', 'effective_steering'),
            info_label('Cruse Ctrl', 'cruse_control'),
            info_label('Left Blinkers', 'left_blinkers'),
            info_label('Right Blinkers', 'right_blinkers'),
            info_label('Beacon', 'light_beacon_icon'),
            info_label('ADAS', 'adas'),
        ]

        layout = [game_info,
                  [PySimpleGUI.Frame('Info', layout=info)],
                  exit_button_layout]

        self.window = PySimpleGUI.Window("ETS2 - ADAS").Layout(layout).Finalize()

    def _update_element(self, key: str, value: str):
        self.window.FindElement(key).Update(value)

    def update_data(self):
        self._update_element('game_name', self._data.get_game_name())
        self._update_element('game_pause', 'paused' if self._data.get_game_pause() else '')

        if self._data.telematic:
            self._update_element('input_steering', format_decimal(self._data.telematic.truck.input_steering))
            # self._update_element('wheel_steering', str(self._data.telematic.truck.effective_steering))
            self._update_element('effective_steering', format_decimal(self._data.telematic.truck.effective_steering))
            self._update_element('cruse_control', format_decimal(self._data.telematic.truck.cruise_control))
            self._update_element('left_blinkers', str(self._data.telematic.truck.lblinker))
            self._update_element('right_blinkers', str(self._data.telematic.truck.rblinker))
            self._update_element('light_beacon_icon', str(self._data.telematic.truck.light_beacon))
            self._update_element('adas', str(self._adas_ok))

    def notify(self, model: ets2.model.Model, event: str):
        # self._log.debug(f"notify({model}, {event})")
        if event == "telematic":
            cc_speed = decimal.Decimal(self._data.telematic.truck.cruise_control)
            cruise_control = not cc_speed.is_zero()
            blinkers = self._data.telematic.truck.lblinker or self._data.telematic.truck.rblinker
            beacon = self._data.telematic.truck.light_beacon
            not_blinkers = not blinkers
            self._adas_ok = cruise_control and not_blinkers and beacon
            #self._log.debug(f"notify: {self._adas_ok} == {cruise_control} and {not_blinkers} ({blinkers}) and {beacon}")
