import decimal
import datetime

import PySimpleGUI

import ets2.model


def wear_info_label(label, key):
    return [PySimpleGUI.Text(label,
                             size=(11, 1),
                             justification="left"),
            PySimpleGUI.Text("---",
                             size=(5, 1),
                             justification="right",
                             key=key)]


def _info_label(label, key):
    return [PySimpleGUI.Text(label,
                             size=(12, 1),
                             justification="left",
                             key=key + "_label"),
            PySimpleGUI.Text('',
                             size=(25, 1),
                             justification="right",
                             key=key)
            ]


class View:
    def __init__(self, data):
        self._data: ets2.model.Model = data
        self._setup_window()
        self._count = 0

    def _setup_window(self):
        job_layout = [
            _info_label('Cargo', 'job_cargo'),
            _info_label('Income', 'job_income'),
            _info_label('Source', 'job_source'),
            _info_label('Destination', 'job_destination'),
            _info_label('Time Left', 'time_left'),
            _info_label('Time to rest', 'time_rest'),
            _info_label('To destination', 'time_dest'),
            _info_label('With Rest', 'time_dest_rest'),
            _info_label('With Timescale', 'time_dest_scale'),
            _info_label('Time', 'game_time'),
            _info_label('Time Scale', 'time_scale'),
        ]
        job_info = [PySimpleGUI.Frame('Job',
                                      size=(80, 6),
                                      layout=job_layout,
                                      key="job")]
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
            _info_label('Left', 'fuel_left'),
            _info_label('Range', 'fuel_range'),
            _info_label('Consumtion', 'fuel_consumtion'),
        ]
        fuel_info = [PySimpleGUI.Frame('Fuel',
                                       size=(80, 6),
                                       layout=fuel_layout)]
        button_layout = [
            [PySimpleGUI.Exit(button_color=('white', 'firebrick4'))]
        ]
        wear_layout_left = [
            wear_info_label('Cabin', "wear_cabin"),
            wear_info_label('Chassis', "wear_chassis"),
            wear_info_label('Engine', "wear_engine"),
            wear_info_label('Transmission', "wear_transmission"),
            wear_info_label('Wheels', "wear_wheels"),
        ]
        wear_layout_right = [
            wear_info_label('Chassis', "wear_trailer"),
            wear_info_label('Wheel', "wear_trailer_wheel"),
            wear_info_label('Cargo', "wear_trailer_cargo"),
        ]
        wear_layout = [
            [PySimpleGUI.Column(layout=[[PySimpleGUI.Frame('Truck', layout=wear_layout_left),
                                         PySimpleGUI.Frame('Trailer', layout=wear_layout_right)]])]
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
            wear_info_label('Pressure', "air_pressure"),
            wear_info_label('Retarder', "brake_retarder"),
            wear_info_label('Temperature', "brake_temperature"),
        ]
        game_info = [PySimpleGUI.Text('',
                                      size=(70, 1),
                                      justification="center",
                                      key="game_name"),
                     PySimpleGUI.Text('',
                                      size=(20, 1),
                                      justification="left",
                                      key="game_pause")
                     ]
        speed_info = [
            PySimpleGUI.Column(layout=speed_layout,
                               # size=(80, 6)
                               )]
        wear_info = [PySimpleGUI.Frame('Wear',
                                       size=(80, 6),
                                       layout=wear_layout)]
        break_info = [PySimpleGUI.Column(layout=brake_info,
                                         # size=(80, 2)
                                         ),
                      ]
        end_layout = [PySimpleGUI.Column(layout=button_layout,
                                         # size=(80, 2),
                                         )]
        map_area = [PySimpleGUI.Graph(canvas_size=(400, 400),
                                      graph_bottom_left=self._data.tracks.bottom_left(),
                                      graph_top_right=self._data.tracks.top_right(),
                                      key='map_canvas')]
        dash_1 = [
            speed_info,
            fuel_info,
            light_icons,
            warning_icons,
            info_icons,
            break_info,
            wear_info,
        ]
        dash_2 = [
            job_info,
            map_area,
        ]

        truck = [_info_label('Brand', "truck_brand"),
                 _info_label('Brand ID', "truck_brand_id"),
                 _info_label('ID', "truck_id"),
                 _info_label('Name', "truck_name"),
                 _info_label('Country', "truck_license_plate_country"),
                 _info_label('Plate', "truck_license_plate"),
                 ]
        trailer_0 = [_info_label('ID', "trailer_id_0"),
                     _info_label('Body', "trailer_body_type"),
                     _info_label('Chain', "trailer_chain_type"),
                     _info_label('Cargo', "trailer_cargo_accessory_id_0"),
                     _info_label('Country', "trailer_license_plate_country_0"),
                     _info_label('Plate', "trailer_license_plate_0"),
                     ]
        trailer_1 = [_info_label('ID', "trailer_id_1"),
                     _info_label('Cargo', "trailer_cargo_accessory_id_1"),
                     _info_label('Country', "trailer_license_plate_country_1"),
                     _info_label('Plate', "trailer_license_plate_1"),
                     ]
        trailer_2 = [_info_label('ID', "trailer_id_2"),
                     _info_label('Cargo', "trailer_cargo_accessory_id_2"),
                     _info_label('Country', "trailer_license_plate_country_2"),
                     _info_label('Plate', "trailer_license_plate_2"),
                     ]
        trailers = [[PySimpleGUI.Frame('Truck', layout=truck)],
                    [PySimpleGUI.Frame('0', layout=trailer_0, key="trailer_0")],
                    [PySimpleGUI.Frame('1', layout=trailer_1, key="trailer_1")],
                    [PySimpleGUI.Frame('2', layout=trailer_2, key="trailer_2")]]
        layout = [game_info,
                  [PySimpleGUI.Column(layout=dash_1),
                   PySimpleGUI.Column(layout=dash_2),
                   PySimpleGUI.Column(layout=trailers),
                   ],
                  end_layout]

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
        if self._data.telematic:
            game_time = datetime.datetime.fromordinal(1) + datetime.timedelta(
                minutes=self._data.telematic.common.game_time)
            self._update_element('game_time', f"{game_time.strftime('%a %H:%M')}")
            self._update_element('time_scale', f"{self._data.telematic.common.scale:.0f}")

        if self._data.job:
            self._update_element('job_cargo',
                                 f'{self._data.job.cargo} ({self._data.job.cargo_mass / 1000:.1f}t)')
            if self._data.game.id == "ats":
                self._update_element('job_income', f'${self._data.job.income}')
            else:
                self._update_element('job_income', f'{self._data.job.income} €')
            self._update_element('job_source', f'{self._data.job.source_company}'
                                               f':{self._data.job.source_city}')
            self._update_element('job_destination', f'{self._data.job.destination_company}'
                                                    f':{self._data.job.destination_city}')

            self._update_element('time_left', format_minute_time(self._data.get_time_left()))
            self._update_element('time_rest', format_minute_time(self._data.get_time_to_rest()))
            self._update_element('time_dest', format_minute_time(self._data.get_time_destination()))
            self._update_element('time_dest_rest', format_minute_time(self._data.get_time_destination_with_rest()))
            if self._data.telematic:
                self._update_element('time_dest_scale',
                                     format_minute_time(int(self._data.get_time_destination()
                                                            / self._data.telematic.common.scale)))
            else:
                self._update_element('time_dest_rest', '')
        else:
            self._update_element('job_cargo', '')
            self._update_element('job_income', '')
            self._update_element('job_source', '')
            self._update_element('job_destination', '')
            self._update_element('time_left', '')
            self._update_element('time_rest', format_minute_time(self._data.get_time_to_rest()))
            self._update_element('time_dest', format_minute_time(self._data.get_time_destination()))
            if self._data.telematic:
                self._update_element('time_dest_rest',
                                     format_minute_time(int(self._data.get_time_destination_with_rest()
                                                            / self._data.telematic.common.scale)))
            else:
                self._update_element('time_dest_rest', '')

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
        if self._data.telematic:
            self._update_element('wear_trailer', format_percent(self._data.telematic.trailer.wear_chassis))
            self._update_element('wear_trailer_wheel', format_percent(self._data.telematic.trailer.wear_wheels))
            self._update_element('wear_trailer_cargo', format_percent(self._data.telematic.trailer.cargo_damage))

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

        if self._data.truck_config:
            self._update_element('truck_brand', self._data.truck_config.brand)
            self._update_element('truck_brand_id', self._data.truck_config.brand_id)
            self._update_element('truck_id', self._data.truck_config.id)
            self._update_element('truck_name', self._data.truck_config.name)
            self._update_element('truck_license_plate_country', self._data.truck_config.license_plate_country)
            self._update_element('truck_license_plate', self._data.truck_config.license_plate)

        if self._data.trailer_config[0]:
            self.window.FindElement("trailer_0").Update(visible=True)
            self._update_element('trailer_id_0', self._data.trailer_config[0].id)
            self._update_element('trailer_body_type', self._data.trailer_config[0].body_type)
            self._update_element('trailer_chain_type', self._data.trailer_config[0].chain_type)
            self._update_element('trailer_cargo_accessory_id_0', self._data.trailer_config[0].cargo_accessory_id)
            self._update_element('trailer_license_plate_country_0', self._data.trailer_config[0].license_plate_country)
            self._update_element('trailer_license_plate_0', self._data.trailer_config[0].license_plate)
        else:
            self.window.FindElement("trailer_0").Update(visible=False)

        if self._data.trailer_config[1]:
            self.window.FindElement("trailer_1").Update(visible=True)
            self._update_element('trailer_id_1', self._data.trailer_config[1].id)
            self._update_element('trailer_cargo_accessory_id_1', self._data.trailer_config[1].cargo_accessory_id)
            self._update_element('trailer_license_plate_country_1', self._data.trailer_config[1].license_plate_country)
            self._update_element('trailer_license_plate_1', self._data.trailer_config[1].license_plate)
        else:
            self.window.FindElement("trailer_1").Update(visible=False)

        if self._data.trailer_config[2]:
            self.window.FindElement("trailer_2").Update(visible=True)
            self._update_element('trailer_id_2', self._data.trailer_config[2].id)
            self._update_element('trailer_cargo_accessory_id_2', self._data.trailer_config[2].cargo_accessory_id)
            self._update_element('trailer_license_plate_country_2', self._data.trailer_config[2].license_plate_country)
            self._update_element('trailer_license_plate_2', self._data.trailer_config[2].license_plate)
        else:
            self.window.FindElement("trailer_2").Update(visible=False)

        self.update_tracks()

    def update_tracks(self):
        self._count += 1
        if self._count % 100:
            return
        tracks = self._data.tracks
        print(len(tracks.points),
              tracks.bottom_left(),
              tracks.top_right())
        canvas: PySimpleGUI.Graph = self.window.FindElement('map_canvas')
        canvas.Erase()
        # canvas.DrawRectangle(top_left=(-99005, -60005),
        #                      bottom_right=(-119999, -65000))
        for point in tracks.points:
            canvas.DrawPoint(point=(point.position.x, point.position.z))


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
