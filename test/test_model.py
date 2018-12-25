import json
from ets2_dash.model import Model
import pytest


def test_getTimeLeftNormal():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    with open("data/job.json", "r") as j:
        model.setJobConfig(json.load(j))
    assert 539 == model.getTimeLeft()

def test_getTimeLeftCommunity():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    with open("data/job_community.json", "r") as j:
        model.setJobConfig(json.load(j))
    assert None == model.getTimeLeft()


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

def test_getCruiseControlKmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.000, abs=0.001) == model.getCruiseControlKmh()

def test_getSpeedLimitKmh():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(48.2, abs=0.1) == model.getSpeedLimitKmh()

def test_getSpeedMph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.003, abs=0.001) == model.getSpeedMph()

def test_getCruiseControlMph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.000, abs=0.001) == model.getCruiseControlMph()

def test_getSpeedLimitMph():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(30.0, abs=0.1) == model.getSpeedLimitMph()

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

def test_getWearCabin():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.005, abs=0.005) == model.getWearCabin()

def test_getWearChassis():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.006, abs=0.005) == model.getWearChassis()

def test_getWearEngine():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.004, abs=0.005) == model.getWearEngine()

def test_getWearTransmission():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.003, abs=0.005) == model.getWearTransmission()

def test_getgetWearWheels():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.015, abs=0.005) == model.getWearWheels()

def test_getWearTrailer():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert pytest.approx(0.00, abs=0.005) == model.getWearTrailer()

def test_getGamePause():
    model = Model()
    with open("data/info.json", "r") as j:
        model.setInfo(json.load(j))
    assert False == model.getGamePause()

def test_getGameName():
    model = Model()
    with open("data/game.json", "r") as j:
        model.setGame(json.load(j))
    assert "Euro Truck Simulator 2 1.33.2.19s" == model.getGameName()

def test_getGameId():
    model = Model()
    with open("data/game.json", "r") as j:
        model.setGame(json.load(j))
    assert "eut2" == model.getGameId()

def test_getLightHighBeam():
    model = Model()
    with open("data/telematic.json", "r") as j:
        model.setTelematicData(json.load(j))
    assert False == model.getLightHighBeam()