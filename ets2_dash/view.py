import decimal

import PySimpleGUI


class View:
    def __init__(self, data):
        self._data = data
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
             PySimpleGUI.Text("556",
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
        layout = [
            [PySimpleGUI.Frame('Job',
                               size=(50, 5),
                               layout=job_layout),
             PySimpleGUI.Column(layout=speed_layout,
                                size=(50, 5))],
            [PySimpleGUI.Frame('Fuel',
                               size=(50, 5),
                               layout=fuel_layout),
             PySimpleGUI.Column(layout=button_layout,
                                size=(50, 5), )],
        ]
        self.window = PySimpleGUI.Window("ETS2 - Telematic Unit").Layout(layout)

    def _updateElement(self, key: str, value: str):
        self.window.FindElement(key).Update(value)

    def updateData(self):
        self._updateElement('time_left', formatMinuteTime(self._data.getTimeLeft()))
        self._updateElement('time_rest', formatMinuteTime(self._data.getTimeToRest()))
        self._updateElement('time_dest', formatMinuteTime(self._data.getTimeDestination()))
        self._updateElement('speed_kmh', formatDecimal(self._data.getSpeedKmh()))
        self._updateElement('speed_mph', formatDecimal(self._data.getSpeedMph()))
        self._updateElement('fuel_left', formatDecimal(self._data.getFuelLeft()))
        self._updateElement('fuel_range', formatDecimal(self._data.getFuelRange()))
        self._updateElement('fuel_consumtion', formatDecimal(self._data.getFuelConsumtion()))


def formatMinuteTime(time):
    hours = time // 60
    mintes = time % 60
    return f"{hours:02d}:{mintes:02d}"


def formatDecimal(value):
    decimal_value = decimal.Decimal(value)
    return f'{decimal_value:.1f}'