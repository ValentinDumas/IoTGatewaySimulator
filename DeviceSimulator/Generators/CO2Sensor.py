import random
from datetime import datetime

class C02Sensor:
    def __init__(self):
        pass

    def GetData(self):
        return random.randrange(0, 500, 1), datetime.now()
