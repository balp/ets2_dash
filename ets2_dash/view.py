import decimal

import PySimpleGUI
import ets2_dash.model


class View:
    def __init__(self, data):
        self._data: ets2_dash.model.Model = data
        self._setup_window()

    def _setup_window(self):
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
                              # font=("Hack Bold", 6),
                              justification="right",
                              key="cc_speed_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              # font=("Hack Bold", 5),
                              justification="left")],
            [PySimpleGUI.Text("Lim",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('60',
                              size=(5, 1),
                              # font=("Hack Bold", 6),
                              justification="right",
                              key="speed_limit_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              # font=("Hack Bold", 5),
                              justification="left")]
        ]
        speed_mph_cc = [
            [PySimpleGUI.Text("CC",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('80.1',
                              size=(5, 1),
                              # font=("Hack Bold", 6),
                              justification="right",
                              key="cc_speed_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              # font=("Hack Bold", 5),
                              justification="left")],
            [PySimpleGUI.Text("Lim",
                              size=(3, 1),
                              justification="left"),
             PySimpleGUI.Text('60',
                              size=(5, 1),
                              # font=("Hack Bold", 6),
                              justification="right",
                              key="speed_limit_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              # font=("Hack Bold", 5),
                              justification="left")]
        ]
        speed_layout = [
            [PySimpleGUI.Column(layout=speed_km_cc),
             PySimpleGUI.Text('80.12',
                              size=(5, 1),
                              # font=("Hack Bold", 10),
                              justification="right",
                              key="speed_kmh"),
             PySimpleGUI.Text("km/h",
                              size=(4, 1),
                              # font=("Hack Bold", 8),
                              justification="left")],
            [PySimpleGUI.Column(layout=speed_mph_cc),
             PySimpleGUI.Text('49.72',
                              size=(5, 1),
                              # font=("Hack Bold", 10),
                              justification="right",
                              key="speed_mph"),
             PySimpleGUI.Text("mph",
                              size=(4, 1),
                              # font=("Hack Bold", 8),
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
                              size=(5, 1),
                              justification="right",
                              key="wear_cabin")],
            [PySimpleGUI.Text('Chassis',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="wear_chassis")],
            [PySimpleGUI.Text('Engine',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="wear_engine")],
        ]
        wear_layout_right = [
            [PySimpleGUI.Text('Transmission',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="wear_transmission")],
            [PySimpleGUI.Text('Wheels',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="wear_wheels")],
            [PySimpleGUI.Text('Trailer',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="wear_trailer")],
        ]
        wear_layout = [
            [PySimpleGUI.Column(layout=[[PySimpleGUI.Column(layout=wear_layout_left),
                                         PySimpleGUI.Column(layout=wear_layout_right)]])]
        ]
        warning_icons = [
            # Malfunctions
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/battery.png",
                              size=(25, 25),
                              key='battery_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/warning.png",
                              size=(25, 25),
                              key='electric_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/malfunction-indicador.png",
                              size=(25, 25),
                              key='engine_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/warning.png",
                              size=(25, 25),
                              key='water_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/oil.png",
                              size=(25, 25),
                              key='oil_icon'),
        ]
        info_icons = [
            # Info
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/winshield-wiper.png",
                              size=(25, 25),
                              key='wipers_icon'),
            # Fuel
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/fuel.png",
                              size=(25, 25),
                              key='adblue_icon'),
            PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/fuel.png",
                              size=(25, 25),
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
        brake_info = [
            # Breaking
            [PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/brake-system-warning.png",
                               size=(25, 25),
                               key='break_emergency'),
             PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/brake-system-warning.png",
                               size=(25, 25),
                               key='break_warning')],
            [PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/hazard.png",
                               size=(25, 25),
                               key='break_parking_icon'),
             PySimpleGUI.Image(filename="/home/balp/src/ets2_dash/ets2_dash/icons/25/warning.png",
                               size=(25, 25),
                               key='brake_engine_icon')],
            [PySimpleGUI.Text('Pressure',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="air_pressure")],
            [PySimpleGUI.Text('Retarder',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="brake_retarder")],
            [PySimpleGUI.Text('Temperature',
                              size=(10, 1),
                              justification="left"),
             PySimpleGUI.Text("---",
                              size=(5, 1),
                              justification="right",
                              key="brake_temperature")],
        ]
        layout = [
            [PySimpleGUI.Text('',
                              size=(70, 1),
                              justification="center",
                              key="game_name"),
             PySimpleGUI.Text('',
                              size=(20, 1),
                              justification="left",
                              key="game_pause")
             ],
            [PySimpleGUI.Frame('Job',
                               size=(80, 6),
                               layout=job_layout),
             PySimpleGUI.Column(layout=speed_layout,
                                # size=(80, 6)
                                )],
            [PySimpleGUI.Frame('Fuel',
                               size=(80, 6),
                               layout=fuel_layout),
             PySimpleGUI.Frame('Wear',
                               size=(80, 6),
                               layout=wear_layout)],
            warning_icons,
            info_icons,
            light_icons,
            [PySimpleGUI.Column(layout=brake_info,
                                # size=(80, 2)
                                ),
             PySimpleGUI.Column(layout=button_layout,
                                # size=(80, 2),
                                )],
        ]
        self.window = PySimpleGUI.Window("ETS2 - Telematic Unit").Layout(layout).Finalize()

    def _update_element(self, key: str, value: str):
        self.window.FindElement(key).Update(value)

    def _update_image(self, key: str, iconname: str, active: bool):
        if active:
            filename = f"/home/balp/src/ets2_dash/ets2_dash/icons/25-on/{iconname}.png"
        else:
            filename = f"/home/balp/src/ets2_dash/ets2_dash/icons/25/{iconname}.png"
        self.window.FindElement(key).Update(filename=filename)

    def update_data(self):
        self._update_element('game_name', self._data.get_game_name())
        self._update_element('game_pause', 'paused' if self._data.get_game_pause() else '')
        self._update_element('time_left', format_minute_time(self._data.get_time_left()))
        self._update_element('time_rest', format_minute_time(self._data.get_time_to_rest()))
        self._update_element('time_dest', format_minute_time(self._data.get_time_destination()))

        self._update_element('cc_speed_kmh', format_decimal(self._data.get_cruise_control_kmh()))
        self._update_element('speed_limit_kmh', format_decimal(self._data.get_speed_limit_kmh()))
        self._update_element('speed_kmh', format_decimal(self._data.get_speed_kmh()))
        self._update_element('cc_speed_mph', format_decimal(self._data.get_cruise_control_mph()))
        self._update_element('speed_limit_mph', format_decimal(self._data.get_speed_limit_mph()))
        self._update_element('speed_mph', format_decimal(self._data.get_speed_mph()))

        self._update_element('fuel_left', format_decimal(self._data.get_fuel_left()))
        self._update_element('fuel_range', format_decimal(self._data.get_fuel_range()))
        self._update_element('fuel_consumtion', format_decimal(self._data.get_fuel_consumtion()))

        self._update_element('wear_cabin', format_percent(self._data.get_wear_cabin()))
        self._update_element('wear_chassis', format_percent(self._data.get_wear_chassis()))
        self._update_element('wear_engine', format_percent(self._data.get_wear_engine()))
        self._update_element('wear_transmission', format_percent(self._data.get_wear_transmission()))
        self._update_element('wear_wheels', format_percent(self._data.get_wear_wheels()))
        self._update_element('wear_trailer', format_percent(self._data.get_wear_trailer()))

        self._update_image('light_beam_high_icon', 'high-beam', self._data.get_light_high_beam())
        self._update_image('light_beam_low_icon', 'low-beam', self._data.get_light_low_beam())
        self._update_image('light_beacon_icon', 'light', self._data.get_light_beacon())
        self._update_image('light_lblinker_icon', 'turn-signals', self._data.get_light_l_blinker())
        self._update_image('light_rblinker_icon', 'turn-signals', self._data.get_light_r_blinker())
        self._update_image('lblinker_icon', 'turn-signals', self._data.get_l_blinker())
        self._update_image('rblinker_icon', 'turn-signals', self._data.get_r_blinker())
        self._update_image('light_parking_icon', 'parking-lights', self._data.get_light_parking())
        self._update_image('light_reverse_icon', 'trunk', self._data.get_light_reverse())
        self._update_image('light_aux_font_icon', 'fog-light', self._data.get_light_aux_front())
        self._update_image('light_aux_roof_icon', 'dome-light', self._data.get_light_aux_roof())
        self._update_image('light_brake_icon', 'glowplug', self._data.get_light_breaking())

        self._update_image('battery_icon', 'battery', self._data.get_battery_warning())
        self._update_image('electric_icon', 'battery', not self._data.get_electric())
        self._update_image('engine_icon', 'malfunction-indicador', not self._data.get_engine())
        self._update_image('water_icon', 'warning', self._data.get_water_warning())
        self._update_image('oil_icon', 'oil', self._data.get_oil_warning())

        self._update_image('wipers_icon', 'winshield-wiper', self._data.get_wipers())
        self._update_image('adblue_icon', 'fuel', self._data.get_ad_blue_warning())
        self._update_image('fuel_icon', 'fuel', self._data.get_fuel_warning())

        self._update_image('break_emergency', 'brake-system-warning', self._data.get_break_emergency())
        self._update_image('break_warning', 'brake-system-warning', self._data.get_break_warning())
        self._update_image('break_parking_icon', 'hazard', self._data.get_break_parking())
        self._update_image('brake_engine_icon', 'warning', self._data.get_break_motor())
        self._update_element('air_pressure', format_decimal(self._data.get_air_pressure()))
        self._update_element('brake_retarder', format_int(self._data.get_break_retarder()))
        self._update_element('brake_temperature', format_decimal(self._data.get_break_temperature()))


def format_minute_time(time):
    if time is None:
        return "---"
    hours = time // 60
    minutes = time % 60
    return f"{hours:02d}:{minutes:02d}"


def format_int(value):
    return f'{value:03d}'


def format_decimal(value):
    decimal_value = decimal.Decimal(value)
    return f'{decimal_value:.1f}'


def format_percent(value):
    per_value = decimal.Decimal(value * 100)
    return f"{per_value:.1f}%"
