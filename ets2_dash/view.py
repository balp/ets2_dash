import decimal

import PySimpleGUI
import ets2_dash.model

class View:
    def __init__(self, data):
        self._data : ets2_dash.model.Model = data
        self._setupWindow()

    def _setupWindow(self):
        job_layout = [
            [PySimpleGUI.Text('Time Left',
                              size=(15, 1),
                              justification="left"),
             PySimpleGUI.Text("21:21",
                              size=(7, 1),
                              justification="right",
                              key="time_left")],
            [PySimpleGUI.Text('Time to rest',
                              size=(15, 1),
                              justification="left"),
             PySimpleGUI.Text("21:21",
                              size=(7, 1),
                              justification="right",
                              key="time_rest")],
            [PySimpleGUI.Text('To destination',
                              size=(15, 1),
                              justification="left"),
             PySimpleGUI.Text("21:21",
                              size=(7, 1),
                              justification="right",
                              key="time_dest")],
        ]
        speed_layout = [
            [PySimpleGUI.Text('80.12',
                              size=(8, 1),
                              font=("Hack Bold", 48),
                              justification="right",
                              key="speed_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              justification="left")],
            [PySimpleGUI.Text('49.72',
                              size=(8, 1),
                              font=("Hack Bold", 48),
                              justification="right",
                              key="speed_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              justification="left")],
        ]
        fuel_layout = [
            [PySimpleGUI.Text('Left',
                              size=(15, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(7, 1),
                              justification="right",
                              key="fuel_left")],
            [PySimpleGUI.Text('Range',
                              size=(15, 1),
                              justification="left"),
             PySimpleGUI.Text("556",
                              size=(7, 1),
                              justification="right",
                              key="fuel_range")],
            [PySimpleGUI.Text('Consumtion',
                              size=(15, 1),
                              justification="left"),
             PySimpleGUI.Text("556",
                              size=(7, 1),
                              justification="right",
                              key="fuel_consumtion")]
        ]
        button_layout = [
            [PySimpleGUI.Exit(button_color=('white', 'firebrick4'))]
        ]
        wear_layout_left = [
            [PySimpleGUI.Text('Cabin',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(4, 1),
                              justification="right",
                              key="wear_cabin")],
            [PySimpleGUI.Text('Chassis',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(4, 1),
                              justification="right",
                              key="wear_chassis")],
            [PySimpleGUI.Text('Engine',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(4, 1),
                              justification="right",
                              key="wear_engine")],
        ]
        wear_layout_right = [
            [PySimpleGUI.Text('Transmission',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(4, 1),
                              justification="right",
                              key="wear_transmission")],
            [PySimpleGUI.Text('Wheels',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(4, 1),
                              justification="right",
                              key="wear_wheels")],
            [PySimpleGUI.Text('Trailer',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(4, 1),
                              justification="right",
                              key="wear_trailer")],
        ]

        wear_layout = [
            [PySimpleGUI.Column(layout=[[PySimpleGUI.Column(layout=wear_layout_left),
                                         PySimpleGUI.Column(layout=wear_layout_right)]])]
        ]
        layout = [
            [PySimpleGUI.Text('',
                              size=(50, 1),
                              justification="center",
                              key="game_name")],
            [PySimpleGUI.Frame('Job',
                               size=(50, 5),
                               layout=job_layout),
             PySimpleGUI.Column(layout=speed_layout,
                                size=(50, 5))],
            [PySimpleGUI.Frame('Fuel',
                               size=(50, 5),
                               layout=fuel_layout),
             PySimpleGUI.Frame('Wear',
                               size=(50, 5),
                               layout=wear_layout)],
            [PySimpleGUI.Text('',
                              size=(10, 1),
                              justification="left",
                              key="game_pause"),
             PySimpleGUI.Column(layout=button_layout,
                                size=(50, 5), )],
        ]
        self.window = PySimpleGUI.Window("ETS2 - Telematic Unit").Layout(layout)

    def _updateElement(self, key: str, value: str):
        self.window.FindElement(key).Update(value)

    def updateData(self):
        self._updateElement('game_name', self._data.getGameName())
        self._updateElement('game_pause', 'paused' if self._data.getGamePause() else '')
        self._updateElement('time_left', formatMinuteTime(self._data.getTimeLeft()))
        self._updateElement('time_rest', formatMinuteTime(self._data.getTimeToRest()))
        self._updateElement('time_dest', formatMinuteTime(self._data.getTimeDestination()))
        self._updateElement('speed_kmh', formatDecimal(self._data.getSpeedKmh()))
        self._updateElement('speed_mph', formatDecimal(self._data.getSpeedMph()))
        self._updateElement('fuel_left', formatDecimal(self._data.getFuelLeft()))
        self._updateElement('fuel_range', formatDecimal(self._data.getFuelRange()))
        self._updateElement('fuel_consumtion', formatDecimal(self._data.getFuelConsumtion()))

        self._updateElement('wear_cabin', formatPercent(self._data.getWearCabin()))
        self._updateElement('wear_chassis', formatPercent(self._data.getWearChassis()))
        self._updateElement('wear_engine', formatPercent(self._data.getWearEngine()))
        self._updateElement('wear_transmission', formatPercent(self._data.getWearTransmission()))
        self._updateElement('wear_wheels', formatPercent(self._data.getWearWheels()))
        self._updateElement('wear_trailer', formatPercent(self._data.getWearTrailer()))


def formatMinuteTime(time):
    if time == None:
        return "---"
    hours = time // 60
    minutes = time % 60
    return f"{hours:02d}:{minutes:02d}"


def formatDecimal(value):
    decimal_value = decimal.Decimal(value)
    return f'{decimal_value:.1f}'

def formatPercent(value):
    per_value = int(value*100)
    return f"{per_value:2d}%"