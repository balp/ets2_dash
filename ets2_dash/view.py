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
        speed_km_cc = [
            [PySimpleGUI.Text("CC",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('80.1',
                              size=(5, 1),
                              font=("Hack Bold", 18),
                              justification="right",
                              key="cc_speed_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              font=("Hack Bold", 6),
                              justification="left")],
            [PySimpleGUI.Text("Lim",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('60',
                              size=(5, 1),
                              font=("Hack Bold", 18),
                              justification="right",
                              key="speed_limit_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              font=("Hack Bold", 6),
                              justification="left")]
        ]
        speed_mph_cc = [
            [PySimpleGUI.Text("CC",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('80.1',
                              size=(5, 1),
                              font=("Hack Bold", 18),
                              justification="right",
                              key="cc_speed_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              font=("Hack Bold", 6),
                              justification="left")],
            [PySimpleGUI.Text("Lim",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('60',
                              size=(5, 1),
                              font=("Hack Bold", 18),
                              justification="right",
                              key="speed_limit_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              font=("Hack Bold", 6),
                              justification="left")]
        ]
        speed_layout = [
            [PySimpleGUI.Column(layout=speed_km_cc),
             PySimpleGUI.Text('80.12',
                              size=(5, 1),
                              font=("Hack Bold", 48),
                              justification="right",
                              key="speed_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              font=("Hack Bold", 10),
                              justification="left")],
            [PySimpleGUI.Column(layout=speed_mph_cc),
             PySimpleGUI.Text('49.72',
                              size=(5, 1),
                              font=("Hack Bold", 48),
                              justification="right",
                              key="speed_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              font=("Hack Bold", 10),
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
        warning_icons = [
            # Malfunctions
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/battery.png",
                              size=(50, 50),
                              key='battery_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/warning.png",
                              size=(50, 50),
                              key='electric_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/malfunction-indicador.png",
                              size=(50, 50),
                              key='engine_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/brake-system-warning.png",
                              size=(50, 50),
                              key='air_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/warning.png",
                              size=(50, 50),
                              key='water_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/oil.png",
                              size=(50, 50),
                              key='oil_icon'),
        ]
        info_icons = [
            # Info
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/winshield-wiper.png",
                              size=(50, 50),
                              key='wipers_icon'),
            # Breaking
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/hazard.png",
                              size=(50, 50),
                              key='break_parking_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/warning.png",
                              size=(50, 50),
                              key='brake_engine_icon'),
            # Fuel
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/fuel.png",
                              size=(50, 50),
                              key='adblue_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/fuel.png",
                              size=(50, 50),
                              key='fuel_icon'),
        ]
        light_icons = [
            # Lights
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/turn-signals.png",
                              size=(25, 25),
                              key='lblinker_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/turn-signals.png",
                              size=(25, 25),
                              key='rblinker_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/turn-signals.png",
                              size=(25, 25),
                              key='light_lblinker_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/turn-signals.png",
                              size=(25, 25),
                              key='light_rblinker_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/dome-light.png",
                              size=(25, 25),
                              key='light_aux_roof_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/fog-light.png",
                              size=(25, 25),
                              key='light_aux_font_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/dome-light.png",
                              size=(25, 25),
                              key='light_beacon_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/high-beam.png",
                              size=(25, 25),
                              key='light_beam_high_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/low-beam.png",
                              size=(25, 25),
                              key='light_beam_low_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/light.png",
                              size=(25, 25),
                              key='light_brake_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/parking-lights.png",
                              size=(25, 25),
                              key='light_parking_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/light.png",
                              size=(25, 25),
                              key='light_reverse_icon'),

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
            warning_icons,
            info_icons,
            light_icons,
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

    def _updateImage(self, key : str, iconname: str, active : bool):
        if active:
            filename = f"/home/balp/src/ets2_dash/ets2_dash/icons/25-on/{iconname}.png"
        else:
            filename = f"/home/balp/src/ets2_dash/ets2_dash/icons/25/{iconname}.png"
        self.window.FindElement(key).Update(filename=filename)

    def updateData(self):
        self._updateElement('game_name', self._data.getGameName())
        self._updateElement('game_pause', 'paused' if self._data.getGamePause() else '')
        self._updateElement('time_left', formatMinuteTime(self._data.getTimeLeft()))
        self._updateElement('time_rest', formatMinuteTime(self._data.getTimeToRest()))
        self._updateElement('time_dest', formatMinuteTime(self._data.getTimeDestination()))

        self._updateElement('cc_speed_kmh', formatDecimal(self._data.getCruiseControlKmh()))
        self._updateElement('speed_limit_kmh', formatDecimal(self._data.getSpeedLimitKmh()))
        self._updateElement('speed_kmh', formatDecimal(self._data.getSpeedKmh()))
        self._updateElement('cc_speed_mph', formatDecimal(self._data.getCruiseControlMph()))
        self._updateElement('speed_limit_mph', formatDecimal(self._data.getSpeedLimitMph()))
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

        self._updateImage('light_beam_high_icon', 'high-beam', self._data.getLightHighBeam())
        self._updateImage('light_beam_low_icon', 'low-beam', self._data.getLightLowBeam())
        self._updateImage('light_beacon_icon', 'light', self._data.getLightBeacon())
        self._updateImage('light_lblinker_icon', 'turn-signals', self._data.getLightLBlinker())
        self._updateImage('light_rblinker_icon', 'turn-signals', self._data.getLightRBlinker())
        self._updateImage('lblinker_icon', 'turn-signals', self._data.getLBlinker())
        self._updateImage('rblinker_icon', 'turn-signals', self._data.getRBlinker())
        self._updateImage('light_parking_icon', 'parking-lights', self._data.getLightParking())
        self._updateImage('light_reverse_icon', 'trunk', self._data.getLightReverse())
        self._updateImage('light_aux_font_icon', 'fog-light', self._data.getLightAuxFront())
        self._updateImage('light_aux_roof_icon', 'dome-light', self._data.getLightAuxRoof())
        self._updateImage('light_brake_icon', 'glowplug', self._data.getLightBreaking())

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
    per_value = decimal.Decimal(value*100)
    return f"{per_value:.1f}%"