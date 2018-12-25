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

    def getSpeedMph(self) -> float:
        if self._telematic:
            if 'truck' in self._telematic and 'truck.speed' in self._telematic['truck']:
                ms = self._telematic['truck']['truck.speed']
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
