from Gateway.Gateway import Gateway

import time
import json
import _thread
import time

g = Gateway()
g.Start(number_of_devices=10)

print("Start Gateway simulation...")

# while(True):
g.Simulate()
    # time.sleep(1)
