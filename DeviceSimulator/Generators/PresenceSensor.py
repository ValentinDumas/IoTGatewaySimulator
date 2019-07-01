import random
from datetime import datetime


class PresenceSensor:
    def __init__(self):
        pass

    def GetData(self):
        return random.randrange(0, 1, 1), datetime.now()
