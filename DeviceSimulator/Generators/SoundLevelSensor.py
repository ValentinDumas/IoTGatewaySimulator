import os
import random
from datetime import datetime


class SoundLevelSensor:
    def __init__(self):
        self.dB = 0
        self.dB_thresholds = [
            (0,   30),
            (20,  50),
            (40,  70),
            (60,  90),
            (80,  110),
            (100, 130)
        ]

        self.random_threshold = self.GetRandomThreshold(self.dB_thresholds)

        self.min_threshold = self.random_threshold[0]
        self.max_threshold = self.random_threshold[1]

        # print(self.random_threshold)
        # print(self.min_threshold)
        # print(self.max_threshold)

    def GetRandomThreshold(self, input_array):
        return random.choice(self.dB_thresholds)

    def GetData(self):
        return random.randrange(self.min_threshold, self.max_threshold, 1), datetime.now()


# soundLevelSensor = SoundLevelSensor()
# print(soundLevelSensor.GetData())

