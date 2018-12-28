class Model:
    def __init__(self):
        self._telematic = None
        self._job = None
        self._info = None
        self._game = None

    def setTelematicData(self, data):
        self._telematic = data

    def setJobConfig(self, data):
        self._job = data

    def setInfo(self, data):
        self._info = data

    def setGame(self, data):
        self._game = data

    def getGamePause(self):
        if self._info:
            if 'paused' in self._info:
                return self._info['paused']
        return None

    def getGameName(self):
        if self._game:
            if 'name' in self._game:
                return self._game['name']
        return None

    def getGameId(self):
        if self._game:
            if 'id' in self._game:
                return self._game['id']
        return None

    def getTimeLeft(self) -> int:
        if self._telematic and self._job:
            game_time = None
            if 'common' in self._telematic and 'game.time' in self._telematic['common']:
                game_time = self._telematic['common']['game.time']
            delivery_time = None
            if 'delivery.time' in self._job:
                delivery_time = self._job['delivery.time']
            if game_time and delivery_time and delivery_time != 0xFFFFFFFF:
                return delivery_time - game_time
        return None

    def getTimeToRest(self) -> int:
        if self._telematic:
            if 'common' in self._telematic and 'rest.stop' in self._telematic['common']:
                return self._telematic['common']['rest.stop']
        return 0

    def getTimeDestination(self) -> int:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.navigation.time' in self._telematic['truck']:
                eta = self._telematic['truck']['truck.navigation.time']
                return int(eta) // 60
        return 0

    def getSpeedKmh(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.speed' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.speed']
                return ms * 3.6
        return 0.0

    def getCruiseControlKmh(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.cruise_control' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.cruise_control']
                return ms * 3.6
        return 0.0

    def getSpeedLimitKmh(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.navigation.speed.limit' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.navigation.speed.limit']
                return ms * 3.6
        return 0.0

    def getSpeedMph(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.speed' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.speed']
                return ms * 2.2369363
        return 0.0

    def getCruiseControlMph(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.cruise_control' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.cruise_control']
                return ms * 2.2369363
        return 0.0

    def getSpeedLimitMph(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.navigation.speed.limit' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.navigation.speed.limit']
                return ms * 2.2369363
        return 0.0

    def getFuelLeft(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.fuel.amount' in self._telematic['truck']:
                return self._telematic['truck']['truck.fuel.amount']
        return 0.0

    def getFuelRange(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.fuel.range' in self._telematic['truck']:
                return self._telematic['truck']['truck.fuel.range']
        return 0.0

    def getFuelConsumtion(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.fuel.consumption.average' in self._telematic['truck']:
                return self._telematic['truck']['truck.fuel.consumption.average']
        return 0.0

    def getWearCabin(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.wear.cabin' in self._telematic['truck']:
                return self._telematic['truck']['truck.wear.cabin']
        return 0.0

    def getWearChassis(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.wear.chassis' in self._telematic['truck']:
                return self._telematic['truck']['truck.wear.chassis']
        return 0.0

    def getWearEngine(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.wear.engine' in self._telematic['truck']:
                return self._telematic['truck']['truck.wear.engine']
        return 0.0

    def getWearTransmission(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.wear.transmission' in self._telematic['truck']:
                return self._telematic['truck']['truck.wear.transmission']
        return 0.0

    def getWearWheels(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.wear.wheels' in self._telematic['truck']:
                return self._telematic['truck']['truck.wear.wheels']
        return 0.0

    def getWearTrailer(self):
        if self._telematic:
            if 'trailer' in self._telematic and 'trailer.wear.chassis' in self._telematic['trailer']:
                return self._telematic['trailer']['trailer.wear.chassis']
        return 0.0

    def getLightHighBeam(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.beam.high' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.beam.high']
        return False

    def getLightLowBeam(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.beam.low' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.beam.low']
        return False

    def getLightBeacon(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.beacon' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.beacon']
        return False

    def getLightLBlinker(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.lblinker' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.lblinker']
        return False

    def getLightRBlinker(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.rblinker' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.rblinker']
        return False

    def getLBlinker(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.lblinker' in self._telematic['truck']:
                return self._telematic['truck']['truck.lblinker']
        return False

    def getRBlinker(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.rblinker' in self._telematic['truck']:
                return self._telematic['truck']['truck.rblinker']
        return False

    def getLightParking(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.parking' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.parking']
        return False

    def getLightReverse(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.reverse' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.reverse']
        return False

    def getLightAuxFront(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.aux.front' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.aux.front']
        return False

    def getLightAuxRoof(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.aux.roof' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.aux.roof']
        return False


    def getLightBreaking(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.light.brake' in self._telematic['truck']:
                return self._telematic['truck']['truck.light.brake']
        return False

    def getADBlueWarning(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.adblue.warning' in self._telematic['truck']:
                return self._telematic['truck']['truck.adblue.warning']
        return False

    def getBreakEmergency(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.air.pressure.emergency' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.air.pressure.emergency']
        return False

    def getBreakWarning(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.air.pressure.warning' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.air.pressure.warning']
        return False

    def getBreakMotor(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.motor' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.motor']
        return False

    def getBreakParking(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.parking' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.parking']
        return False


    def getElectric(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.electric.enabled' in self._telematic['truck']:
                return self._telematic['truck']['truck.electric.enabled']
        return False

    def getBatteryWarning(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.battery.voltage.warning' in self._telematic['truck']:
                return self._telematic['truck']['truck.battery.voltage.warning']
        return False

    def getEngine(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.engine.enabled' in self._telematic['truck']:
                return self._telematic['truck']['truck.engine.enabled']
        return False


    def getFuelWarning(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.fuel.warning' in self._telematic['truck']:
                return self._telematic['truck']['truck.fuel.warning']
        return False


    def getOilWarning(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.oil.pressure.warning' in self._telematic['truck']:
                return self._telematic['truck']['truck.oil.pressure.warning']
        return False


    def getWaterWarning(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.water.temperature.warning' in self._telematic['truck']:
                return self._telematic['truck']['truck.water.temperature.warning']
        return False


    def getWipers(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.wipers' in self._telematic['truck']:
                return self._telematic['truck']['truck.wipers']
        return False

    def getAirPressure(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.air.pressure' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.air.pressure']
        return False

    def getBreakRetarder(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.retarder' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.retarder']
        return False


    def getBreakTemperature(self):
        if self._telematic:
            if 'truck' in self._telematic and 'truck.brake.temperature' in self._telematic['truck']:
                return self._telematic['truck']['truck.brake.temperature']
        return False


