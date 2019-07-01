import random
from datetime import datetime

class GPSSensor:
    def __init__(self):
        self.nmea = "NMEA0183:AE;3N:6D:OO;3E"
        pass

    def GetData(self):
        return self.nmea, datetime.now()
