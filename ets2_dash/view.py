import decimal
import datetime
import logging
import sys
from pathlib import Path

import PySimpleGUI

import ets2.model
import ets2.work_log
from ets2.types import Vector, vector_min, vector_max, vector_abs_delta, vector_multiply, vector_add, vector_div


#
# -> In world space the X points to east, Y up and Z south.
#
#                           0,width
#    +-----------------------+
#    |min_x,min_y            |
#    |                       |
#    |                       |
#    |            max_x,max_y|
#    +-----------------------+
#    0,height
#
#

COLORS = ['snow', 'ghost white', 'white smoke', 'gainsboro', 'floral white', 'old lace',
          'linen', 'antique white', 'papaya whip', 'blanched almond', 'bisque', 'peach puff',
          'navajo white', 'lemon chiffon', 'mint cream', 'azure', 'alice blue', 'lavender',
          'lavender blush', 'misty rose', 'dark slate gray', 'dim gray', 'slate gray',
          'light slate gray', 'gray', 'light gray', 'midnight blue', 'navy', 'cornflower blue', 'dark slate blue',
          'slate blue', 'medium slate blue', 'light slate blue', 'medium blue', 'royal blue', 'blue',
          'dodger blue', 'deep sky blue', 'sky blue', 'light sky blue', 'steel blue', 'light steel blue',
          'light blue', 'powder blue', 'pale turquoise', 'dark turquoise', 'medium turquoise', 'turquoise',
          'cyan', 'light cyan', 'cadet blue', 'medium aquamarine', 'aquamarine', 'dark green', 'dark olive green',
          'dark sea green', 'sea green', 'medium sea green', 'light sea green', 'pale green', 'spring green',
          'lawn green', 'medium spring green', 'green yellow', 'lime green', 'yellow green',
          'forest green', 'olive drab', 'dark khaki', 'khaki', 'pale goldenrod', 'light goldenrod yellow',
          'light yellow', 'yellow', 'gold', 'light goldenrod', 'goldenrod', 'dark goldenrod', 'rosy brown',
          'indian red', 'saddle brown', 'sandy brown',
          'dark salmon', 'salmon', 'light salmon', 'orange', 'dark orange',
          'coral', 'light coral', 'tomato', 'orange red', 'red', 'hot pink', 'deep pink', 'pink', 'light pink',
          'pale violet red', 'maroon', 'medium violet red', 'violet red',
          'medium orchid', 'dark orchid', 'dark violet', 'blue violet', 'purple', 'medium purple',
          'thistle', 'snow2', 'snow3',
          'snow4', 'seashell2', 'seashell3', 'seashell4', 'AntiqueWhite1', 'AntiqueWhite2',
          'AntiqueWhite3', 'AntiqueWhite4', 'bisque2', 'bisque3', 'bisque4', 'PeachPuff2',
          'PeachPuff3', 'PeachPuff4', 'NavajoWhite2', 'NavajoWhite3', 'NavajoWhite4',
          'LemonChiffon2', 'LemonChiffon3', 'LemonChiffon4', 'cornsilk2', 'cornsilk3',
          'cornsilk4', 'ivory2', 'ivory3', 'ivory4', 'honeydew2', 'honeydew3', 'honeydew4',
          'LavenderBlush2', 'LavenderBlush3', 'LavenderBlush4', 'MistyRose2', 'MistyRose3',
          'MistyRose4', 'azure2', 'azure3', 'azure4', 'SlateBlue1', 'SlateBlue2', 'SlateBlue3',
          'SlateBlue4', 'RoyalBlue1', 'RoyalBlue2', 'RoyalBlue3', 'RoyalBlue4', 'blue2', 'blue4',
          'DodgerBlue2', 'DodgerBlue3', 'DodgerBlue4', 'SteelBlue1', 'SteelBlue2',
          'SteelBlue3', 'SteelBlue4', 'DeepSkyBlue2', 'DeepSkyBlue3', 'DeepSkyBlue4',
          'SkyBlue1', 'SkyBlue2', 'SkyBlue3', 'SkyBlue4', 'LightSkyBlue1', 'LightSkyBlue2',
          'LightSkyBlue3', 'LightSkyBlue4', 'Slategray1', 'Slategray2', 'Slategray3',
          'Slategray4', 'LightSteelBlue1', 'LightSteelBlue2', 'LightSteelBlue3',
          'LightSteelBlue4', 'LightBlue1', 'LightBlue2', 'LightBlue3', 'LightBlue4',
          'LightCyan2', 'LightCyan3', 'LightCyan4', 'PaleTurquoise1', 'PaleTurquoise2',
          'PaleTurquoise3', 'PaleTurquoise4', 'CadetBlue1', 'CadetBlue2', 'CadetBlue3',
          'CadetBlue4', 'turquoise1', 'turquoise2', 'turquoise3', 'turquoise4', 'cyan2', 'cyan3',
          'cyan4', 'DarkSlategray1', 'DarkSlategray2', 'DarkSlategray3', 'DarkSlategray4',
          'aquamarine2', 'aquamarine4', 'DarkSeaGreen1', 'DarkSeaGreen2', 'DarkSeaGreen3',
          'DarkSeaGreen4', 'SeaGreen1', 'SeaGreen2', 'SeaGreen3', 'PaleGreen1', 'PaleGreen2',
          'PaleGreen3', 'PaleGreen4', 'SpringGreen2', 'SpringGreen3', 'SpringGreen4',
          'green2', 'green3', 'green4', 'chartreuse2', 'chartreuse3', 'chartreuse4',
          'OliveDrab1', 'OliveDrab2', 'OliveDrab4', 'DarkOliveGreen1', 'DarkOliveGreen2',
          'DarkOliveGreen3', 'DarkOliveGreen4', 'khaki1', 'khaki2', 'khaki3', 'khaki4',
          'LightGoldenrod1', 'LightGoldenrod2', 'LightGoldenrod3', 'LightGoldenrod4',
          'LightYellow2', 'LightYellow3', 'LightYellow4', 'yellow2', 'yellow3', 'yellow4',
          'gold2', 'gold3', 'gold4', 'goldenrod1', 'goldenrod2', 'goldenrod3', 'goldenrod4',
          'DarkGoldenrod1', 'DarkGoldenrod2', 'DarkGoldenrod3', 'DarkGoldenrod4',
          'RosyBrown1', 'RosyBrown2', 'RosyBrown3', 'RosyBrown4', 'IndianRed1', 'IndianRed2',
          'IndianRed3', 'IndianRed4', 'sienna1', 'sienna2', 'sienna3', 'sienna4', 'burlywood1',
          'burlywood2', 'burlywood3', 'burlywood4', 'wheat1', 'wheat2', 'wheat3', 'wheat4', 'tan1',
          'tan2', 'tan4', 'chocolate1', 'chocolate2', 'chocolate3', 'firebrick1', 'firebrick2',
          'firebrick3', 'firebrick4', 'brown1', 'brown2', 'brown3', 'brown4', 'salmon1', 'salmon2',
          'salmon3', 'salmon4', 'LightSalmon2', 'LightSalmon3', 'LightSalmon4', 'orange2',
          'orange3', 'orange4', 'DarkOrange1', 'DarkOrange2', 'DarkOrange3', 'DarkOrange4',
          'coral1', 'coral2', 'coral3', 'coral4', 'tomato2', 'tomato3', 'tomato4', 'OrangeRed2',
          'OrangeRed3', 'OrangeRed4', 'red2', 'red3', 'red4', 'DeepPink2', 'DeepPink3', 'DeepPink4',
          'HotPink1', 'HotPink2', 'HotPink3', 'HotPink4', 'pink1', 'pink2', 'pink3', 'pink4',
          'LightPink1', 'LightPink2', 'LightPink3', 'LightPink4', 'PaleVioletRed1',
          'PaleVioletRed2', 'PaleVioletRed3', 'PaleVioletRed4', 'maroon1', 'maroon2',
          'maroon3', 'maroon4', 'VioletRed1', 'VioletRed2', 'VioletRed3', 'VioletRed4',
          'magenta2', 'magenta3', 'magenta4', 'orchid1', 'orchid2', 'orchid3', 'orchid4', 'plum1',
          'plum2', 'plum3', 'plum4', 'MediumOrchid1', 'MediumOrchid2', 'MediumOrchid3',
          'MediumOrchid4', 'DarkOrchid1', 'DarkOrchid2', 'DarkOrchid3', 'DarkOrchid4',
          'purple1', 'purple2', 'purple3', 'purple4', 'MediumPurple1', 'MediumPurple2',
          'MediumPurple3', 'MediumPurple4', 'thistle1', 'thistle2', 'thistle3', 'thistle4',
          'grey1', 'grey2', 'grey3', 'grey4', 'grey5', 'grey6', 'grey7', 'grey8', 'grey9', 'grey10',
          'grey11', 'grey12', 'grey13', 'grey14', 'grey15', 'grey16', 'grey17', 'grey18', 'grey19',
          'grey20', 'grey21', 'grey22', 'grey23', 'grey24', 'grey25', 'grey26', 'grey27', 'grey28',
          'grey29', 'grey30', 'grey31', 'grey32', 'grey33', 'grey34', 'grey35', 'grey36', 'grey37',
          'grey38', 'grey39', 'grey40', 'grey42', 'grey43', 'grey44', 'grey45', 'grey46', 'grey47',
          'grey48', 'grey49', 'grey50', 'grey51', 'grey52', 'grey53', 'grey54', 'grey55', 'grey56',
          'grey57', 'grey58', 'grey59', 'grey60', 'grey61', 'grey62', 'grey63', 'grey64', 'grey65',
          'grey66', 'grey67', 'grey68', 'grey69', 'grey70', 'grey71', 'grey72', 'grey73', 'grey74',
          'grey75', 'grey76', 'grey77', 'grey78', 'grey79', 'grey80', 'grey81', 'grey82', 'grey83',
          'grey84', 'grey85', 'grey86', 'grey87', 'grey88', 'grey89', 'grey90', 'grey91', 'grey92',
          'grey93', 'grey94', 'grey95', 'grey97', 'grey98', 'grey99']

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
    def __init__(self, model: ets2.model.Model, work_log: ets2.work_log.WorkLog):
        self._data: ets2.model.Model = model
        self._work_log: ets2.work_log.WorkLog = work_log
        self._log = logging.getLogger("view")

        # TODO: Get the icon location someplace better, e.g. install with program
        self._icons_folder = Path("C:\\Users\\ander\\PycharmProjects\\ets2_dash\\ets2_dash\\icons")
        # self._icons_folder = Path("/home/balp/src/ets2_dash/ets2_dash/icons/")
        self._map_width = 400
        self._map_height = 400
        self._map_virtual_width = 1000
        self._map_virtual_height = 1000
        self._bottom_left = (0, self._map_virtual_width)
        self._top_right = (self._map_virtual_height, 0)

        # Uses self._icons_folder so have to be after
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
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('battery.png')}",
                              size=(25, 25),
                              key='battery_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('warning.png')}",
                              size=(25, 25),
                              key='electric_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('malfunction-indicador.png')}",
                              size=(25, 25),
                              key='engine_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('warning.png')}",
                              size=(25, 25),
                              key='water_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('oil.png')}",
                              size=(25, 25),
                              key='oil_icon'),
        ]
        info_icons = [
            # Info
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('winshield-wiper.png')}",
                              size=(25, 25),
                              key='wipers_icon'),
            # Fuel
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('fuel.png')}",
                              size=(25, 25),
                              key='adblue_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('fuel.png')}",
                              size=(25, 25),
                              key='fuel_icon'),
        ]
        light_icons = [
            # Lights
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('turn-signals.png')}",
                              size=(25, 25),
                              key='lblinker_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('turn-signals.png')}",
                              size=(25, 25),
                              key='rblinker_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('turn-signals.png')}",
                              size=(25, 25),
                              key='light_lblinker_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('turn-signals.png')}",
                              size=(25, 25),
                              key='light_rblinker_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('dome-light.png')}",
                              size=(25, 25),
                              key='light_aux_roof_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('fog-light.png')}",
                              size=(25, 25),
                              key='light_aux_font_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('dome-light.png')}",
                              size=(25, 25),
                              key='light_beacon_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('high-beam.png')}",
                              size=(25, 25),
                              key='light_beam_high_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('low-beam.png')}",
                              size=(25, 25),
                              key='light_beam_low_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('light.png')}",
                              size=(25, 25),
                              key='light_brake_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('parking-lights.png')}",
                              size=(25, 25),
                              key='light_parking_icon'),
            PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('light.png')}",
                              size=(25, 25),
                              key='light_reverse_icon'),

        ]
        brake_info = [
            # Breaking
            [PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('brake-system-warning.png')}",
                               size=(25, 25),
                               key='break_emergency'),
             PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('brake-system-warning.png')}",
                               size=(25, 25),
                               key='break_warning')],
            [PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('hazard.png')}",
                               size=(25, 25),
                               key='break_parking_icon'),
             PySimpleGUI.Image(filename=f"{self._icons_folder / Path('25') / Path('warning.png')}",
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
        map_area = [PySimpleGUI.Graph(canvas_size=(self._map_width, self._map_height),
                                      graph_bottom_left=self._bottom_left,
                                      graph_top_right=self._top_right,
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
            # filename = f"/home/balp/src/ets2_dash/ets2_dash/icons/25-on/{iconname}.png"
            filename = f"C:\\Users\\ander\\PycharmProjects\\ets2_dash\\ets2_dash\\icons\\25-on\\{iconname}.png"
        else:
            # filename = f"/home/balp/src/ets2_dash/ets2_dash/icons/25/{iconname}.png"
            filename = f"C:\\Users\\ander\\PycharmProjects\\ets2_dash\\ets2_dash\\icons\\25\\{iconname}.png"
        self.window.FindElement(key).Update(filename=filename)

    def update_data(self):
        #self._log.debug("update_data")
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
        canvas: PySimpleGUI.Graph = self.window.FindElement('map_canvas')
        canvas.Erase()
        canvas.draw_rectangle(self._top_right, self._bottom_left, line_color='grey80', line_width=3)

        tracks = self._data.tracks

        min_pos = Vector(sys.float_info.max, sys.float_info.max, sys.float_info.max)
        max_pos = Vector(-sys.float_info.max, -sys.float_info.max, -sys.float_info.max)
        for count, job in enumerate(self._work_log.jobs):
            job_min_pos = job.track.min()
            job_max_pos = job.track.max()
            min_pos = vector_min(min_pos, job_min_pos)
            max_pos = vector_max(max_pos, job_max_pos)
        min_pos = vector_min(min_pos, tracks.min())
        max_pos = vector_max(max_pos, tracks.max())

        delta = vector_abs_delta(min_pos, max_pos)
        self._log.info(f"delta: {delta}")
        if delta.x == 0 or delta.z == 0 or delta.y == 0.0:
            return
        scale = vector_div(Vector(self._map_virtual_width, 1, self._map_virtual_height), delta)
        offset = Vector(-min_pos.x, -min_pos.y, -min_pos.z)

        for count, job in enumerate(self._work_log.jobs):
            color = COLORS[count % len(COLORS)]
            _draw_track(canvas, job.track.points, color, offset, scale)

        color = 'grey66'
        _draw_track(canvas, tracks.points, color, offset, scale)
        if len(tracks.points):
            last_point = tracks.points[-1]
            p = vector_multiply(vector_add(last_point.position, offset), scale)
            last_pos = (p.x, p.z)
            canvas.draw_circle(last_pos, radius=10, fill_color=None, line_color='cyan2', line_width=2)

    def notify(self, model: ets2.model.Model, event: str):
        pass


def _draw_track(canvas, points, color, offset, scale):
    for point in points:
        p = vector_multiply(vector_add(point.position, offset), scale)
        position = (p.x, p.z)
        canvas.draw_point(point=position,
                          size=2,
                          color=color, )


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
