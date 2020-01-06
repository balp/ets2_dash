import json
import pprint

from approvaltests import verify

from ets2_dash.model import Model
import pytest


def test_get_time_left_normal():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    model.set_job_config(json.loads("{}"))
    assert model.get_time_left() is None


def test_get_time_left_community():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    with open("data/job_community.json", "r") as j:
        model.set_job_config(json.load(j))
    assert model.get_time_left() is None


def test_get_time_to_rest():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_time_to_rest() == 63


def test_get_time_destination_freeride():
    model = Model()
    with open("data/telematic_freeride.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_time_destination() == 100


def test_get_time_destination():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_time_destination() == 0


def test_get_time_destination_with_rest_no_rest():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_time_destination_with_rest() == 0


def test_get_time_destination_with_rest_needs_rest():
    model = Model()
    with open("data/telematic_reststop.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert 1263 == model.get_time_destination_with_rest()


def test_get_speed_kmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_speed_kmh() == pytest.approx(16.1, abs=0.1)


def test_get_cruise_control_kmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.000, abs=0.001) == model.get_cruise_control_kmh()


def test_get_speed_limit_kmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_speed_limit_kmh() == pytest.approx(0.0, abs=0.1)


def test_get_speed_mph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_speed_mph() == pytest.approx(10.0, abs=0.1)


def test_get_cruise_control_mph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.000, abs=0.001) == model.get_cruise_control_mph()


def test_get_speed_limit_mph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_speed_limit_mph() == pytest.approx(0.0, abs=0.1)


def test_get_fuel_left():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_fuel_left() == pytest.approx(142.3, abs=0.05)


def test_get_fuel_range():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_fuel_range() == pytest.approx(444.6, abs=0.05)


def test_get_fuel_consumtion():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_fuel_consumtion() == pytest.approx(0.5, abs=0.1)


def test_get_wear_cabin():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.005, abs=0.005) == model.get_wear_cabin()


def test_get_wear_chassis():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.006, abs=0.005) == model.get_wear_chassis()


def test_get_wear_engine():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.004, abs=0.005) == model.get_wear_engine()


def test_get_wear_transmission():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.003, abs=0.005) == model.get_wear_transmission()


def test_get_wear_wheels():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_wear_wheels() == pytest.approx(0.005, abs=0.001)


def test_get_wear_trailer():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.00, abs=0.005) == model.get_wear_trailer()


def test_get_game_pause():
    model = Model()
    with open("data/info.json", "r") as j:
        model.set_info(json.load(j))
    assert not model.get_game_pause()


def test_get_game_name():
    model = Model()
    with open("data/game.json", "r") as j:
        model.set_game(json.load(j))
    assert "Euro Truck Simulator 2 1.33.2.19s" == model.get_game_name()


def test_get_game_id():
    model = Model()
    with open("data/game.json", "r") as j:
        model.set_game(json.load(j))
    assert "eut2" == model.get_game_id()


def test_get_light_high_beam():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_high_beam()


def test_get_light_low_beam():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_light_low_beam()


def test_get_light_beacon():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_beacon()


def test_get_light_l_blinker():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_l_blinker()


def test_get_light_r_blinker():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_r_blinker()


def test_get_light_parking():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_light_parking()


def test_get_light_reverse():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_reverse()


def test_get_light_aux_front():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_light_aux_front()


def test_get_light_aux_roof():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_light_aux_roof()


def test_get_light_breaking():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_breaking()


def test_get_l_blinker():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_l_blinker()


def test_get_r_blinker():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_r_blinker()


def test_get_ad_blue_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_ad_blue_warning()


def test_get_break_motor_breaking():
    model = Model()
    with open("data/telematic_breaking.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_motor()


def test_get_break_motor_breaking_engine():
    model = Model()
    with open("data/telematic_engine_break.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_break_motor()


def test_get_break_motor():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_motor()


def test_get_break_parking():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_parking()


def test_get_electric():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_electric()


def test_get_battery_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_battery_warning()


def test_get_engine():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_engine()


def test_get_fuel_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_fuel_warning()


def test_get_oil_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_oil_warning()


def test_get_water_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_water_warning()


def test_get_wipers():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_wipers()


def test_get_break_emergency():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_emergency()


def test_get_break_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_warning()


def test_get_air_pressure():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_air_pressure() == pytest.approx(115.5, abs=0.5)


def test_get_break_retarder():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0, abs=0.5) == model.get_break_retarder()


def test_get_break_temperature():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_break_temperature() == pytest.approx(27.8, abs=0.5)


def test_get_break_warning_1_01():
    model = Model()
    with open("data/telematic_1_01.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_warning()


def test_dual_trailer_config():
    model = Model()
    with open("data/trailer_dual_0.json", "r") as t0:
        model.set_trailer_config(json.load(t0), 0)
    with open("data/trailer_dual_1.json", "r") as t1:
        model.set_trailer_config(json.load(t1), 1)
    assert model.trailer_config[0] is not None
    assert model.trailer_config[1] is not None
    assert model.trailer_config[2] is None


def test_no_trailer():
    model = Model()
    data = json.loads("{}")
    pprint.pprint(data)
    model.set_trailer_config(data, 0)
    model.set_trailer_config(data, 1)
    model.set_trailer_config(data, 1)
    assert model.trailer_config[0] is None
    assert model.trailer_config[1] is None
    assert model.trailer_config[2] is None


def test_add_job():
    model = Model()
    with open("data/job_1.01.json", "r") as j:
        model.set_job_config(json.load(j))
    assert model.job.income == 24293


def test_add_no_job():
    model = Model()
    model.set_job_config(json.loads("{}"))
    assert model.job is None


def test_inital_track():
    model = Model()
    files = ["data/telematic.json",
             "data/telematic_1_01.json",
             "data/telematic_breaking.json",
             "data/telematic_engine_break.json",
             "data/telematic_freeride.json",
             "data/telematic_reststop.json"]
    for f in files:
        with open(f, "r") as j:
            model.set_telematic_data(json.load(j))
    verify(str(model.tracks))


def test_inital_track_bottom_left_corner_empty():
    model = Model()
    assert model.tracks.bottom_left() == (-100000, -5)

def test_inital_track_bottom_left_corner():
    model = Model()
    files = ["data/telematic.json",
             "data/telematic_1_01.json",
             "data/telematic_breaking.json",
             "data/telematic_engine_break.json",
             "data/telematic_freeride.json",
             "data/telematic_reststop.json"]
    for f in files:
        with open(f, "r") as j:
            model.set_telematic_data(json.load(j))
    assert model.tracks.bottom_left() == (-38626.81513977051, -1.187657356262207)

def test_inital_track_top_right_corner_empty():
    model = Model()
    assert model.tracks.top_right() == (61000, 30)


def test_inital_track_top_right_corner():
    model = Model()
    files = ["data/telematic.json",
             "data/telematic_1_01.json",
             "data/telematic_breaking.json",
             "data/telematic_engine_break.json",
             "data/telematic_freeride.json",
             "data/telematic_reststop.json"]
    for f in files:
        with open(f, "r") as j:
            model.set_telematic_data(json.load(j))
    assert model.tracks.top_right() == (60740.99865722656, 28.410934448242188)
