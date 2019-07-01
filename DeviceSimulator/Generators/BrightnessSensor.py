import random
from datetime import datetime

class BrightnessSensor:
    def __init__(self):
        pass

    def GetData(self):
        return random.randrange(0, 255, 1), datetime.now()
