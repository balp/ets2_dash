import json
from ets2_dash.model import Model
import pytest


def test_getTimeLeft():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    with open("data/job.json", "r") as j:
        model.setJobConfig(json.load(j))
    assert 539 == model.getTimeLeft()


def test_getTimeToRest():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert 450 == model.getTimeToRest()


def test_getTimeDestination():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert 283 == model.getTimeDestination()


def test_getSpeedKmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.003, abs=0.001) == model.getSpeedKmh()


def test_getSpeedMph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.003, abs=0.001) == model.getSpeedMph()


def test_getFuelLeft():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(556.5, abs=0.05) == model.getFuelLeft()


def test_getFuelRange():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(1739.1, abs=0.05) == model.getFuelRange()


def test_getFuelConsumtion():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.66, abs=0.005) == model.getFuelConsumtion()
