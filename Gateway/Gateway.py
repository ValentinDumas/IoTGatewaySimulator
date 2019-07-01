import os
import json

# TODO: RabbitMQ

from DeviceSimulator.Models.Device import Device
from DeviceSimulator.DeviceSimulator import DeviceSimulator

from Requests.Send import *
from Requests.Receive import *
from Requests.PostRequest import *

# @TODO: Receive created device
# @TODO:

from DeviceSimulator.Generators.MacAddressGenerator import MacAddressGenerator, MacAddressGeneratorOptimized


class Gateway:
    def __init__(self):
        self.mac_address_generator = MacAddressGenerator()
        self.mac_domain = self.mac_address_generator.GenerateMacAddress()
        self.mac_address = self.mac_domain # Gateway has same mac for "domain" and "device"
        self.deviceSimulator = DeviceSimulator(macDomain=self.mac_domain, macAddressGenerator=self.mac_address_generator)
        self.current_json_data = ""


    def Start(self, number_of_devices):
        self.deviceSimulator.Start(number_of_devices)


    # TODO: Send every 10 seconds the data from N devices connected to the current Gateway instance
    # TODO: Call this method at a 5 or 10 seconds' intervals
    def Simulate(self):
        self.deviceSimulator.Simulate()  # Update and (Re-)Compile device data
        print("devices:",str(len(self.deviceSimulator.devicePool.devices)))
