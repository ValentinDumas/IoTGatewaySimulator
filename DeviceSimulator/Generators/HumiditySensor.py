import random
from datetime import datetime

class HumiditySensor:
    def __init__(self):
        pass

    def GetData(self):
        return random.randrange(0, 100, 1), datetime.now()
