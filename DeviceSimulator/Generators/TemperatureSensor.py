import random
from datetime import datetime

# @TODO: play with different hours of the day

class TemperatureSensor:
    def __init__(self):
        pass

    def GetData(self):
        return 25, datetime.now() # 25°C at T time (now)
