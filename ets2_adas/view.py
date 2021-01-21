import decimal
import datetime
import logging
from pathlib import Path

import PySimpleGUI
import ets2.model


class View:
    def __init__(self, data: ets2.model.Model):
        self._data: ets2.model.Model = data
        self._log = logging.getLogger("view")

        layout = [PySimpleGUI.Exit(button_color=('white', 'firebrick4'))]

        self.window = PySimpleGUI.Window("ETS2 - ADAS").Layout(layout).Finalize()

    def notify(self, model: ets2.model.Model, event: str):
        self._log.debug(f"notify()")

