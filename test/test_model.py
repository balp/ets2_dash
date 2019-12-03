import json
from ets2_dash.model import Model
import pytest


def test_get_time_left_normal():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    with open("data/job.json", "r") as j:
        model.set_job_config(json.load(j))
    assert 539 == model.get_time_left()


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
    assert 450 == model.get_time_to_rest()


def test_get_time_destination_freeride():
    model = Model()
    with open("data/telematic_freeride.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_time_destination() == 100


def test_get_time_destination():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert 283 == model.get_time_destination()


def test_get_time_destination_with_rest_no_rest():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert 283 == model.get_time_destination_with_rest()


def test_get_time_destination_with_rest_needs_rest():
    model = Model()
    with open("data/telematic_reststop.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert 1263 == model.get_time_destination_with_rest()


def test_get_speed_kmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.003, abs=0.001) == model.get_speed_kmh()


def test_get_cruise_control_kmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.000, abs=0.001) == model.get_cruise_control_kmh()


def test_get_speed_limit_kmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(48.2, abs=0.1) == model.get_speed_limit_kmh()


def test_get_speed_mph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.003, abs=0.001) == model.get_speed_mph()


def test_get_cruise_control_mph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.000, abs=0.001) == model.get_cruise_control_mph()


def test_get_speed_limit_mph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(30.0, abs=0.1) == model.get_speed_limit_mph()


def test_get_fuel_left():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(556.5, abs=0.05) == model.get_fuel_left()


def test_get_fuel_range():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(1739.1, abs=0.05) == model.get_fuel_range()


def test_get_fuel_consumtion():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0.66, abs=0.005) == model.get_fuel_consumtion()


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
    assert pytest.approx(0.015, abs=0.005) == model.get_wear_wheels()


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
    assert not model.get_light_aux_front()


def test_get_light_aux_roof():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_light_aux_roof()


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
    assert model.get_break_parking()


def test_get_electric():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_electric()


def test_get_battery_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_battery_warning()


def test_get_engine():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_engine()


def test_get_fuel_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_fuel_warning()


def test_get_oil_warning():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert model.get_oil_warning()


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
    assert pytest.approx(124.4, abs=0.5) == model.get_air_pressure()


def test_get_break_retarder():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(0, abs=0.5) == model.get_break_retarder()


def test_get_break_temperature():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert pytest.approx(18, abs=0.5) == model.get_break_temperature()

def test_get_break_warning_1_01():
    model = Model()
    with open("data/telematic_1_01.json", "r") as j:
        model.set_telematic_data(json.load(j))
    assert not model.get_break_warning()