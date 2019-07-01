import random
from datetime import datetime


class AtmosphericPressureSensor:
    def __init__(self):
        self.hPa = 1013.25

    def GetData(self):
        return random.randrange(int(self.hPa) - 3, int(self.hPa) + 3), datetime.now()
