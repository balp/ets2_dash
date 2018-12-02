class Model:
    def __init__(self):
        self._telematic = None
        self._job = None

    def setTelematicData(self, data):
        self._telematic = data

    def setJobConfig(self, data):
        self._job = data

    def getTimeLeft(self) -> int:
        if self._telematic and self._job:
            game_time = None
            if 'common' in self._telematic and 'game.time' in self._telematic['common']:
                game_time = self._telematic['common']['game.time']
            delivery_time = None
            if 'delivery.time' in self._job:
                delivery_time = self._job['delivery.time']
            if game_time and delivery_time:
                return delivery_time - game_time
        return 0

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