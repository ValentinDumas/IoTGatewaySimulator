import json

from DeviceSimulator.Models.DevicePool import DevicePool
from DeviceSimulator.Models.DeviceFactory import DeviceFactory

from Requests.Send import *
from Requests.Receive import *
from Requests.PostRequest import *

NET_PLATFORM_ENDPOINT = "localhost"
RABBITMQ_ENDPOINT = "localhost"

QUEUE_NAME_TELEMETRY = 'task_queue'
QUEUE_NAME_COMMAND = 'command_queue'


class DeviceSimulator:
    def __init__(self, macDomain, macAddressGenerator):
        self.macDomain = macDomain
        self.devicePool = DevicePool()
        self.deviceFactory = DeviceFactory(macAddressGenerator)

        self.json_devices_telemetry = []


    def GetDevicesTelemetryAsJson(self):
        for device in self.devicePool.devices:
            if device.telemetry.metricValue != None:
                self.json_devices_telemetry.append({"id_device": device.id, "value": str(device.telemetry.metricValue), "date": "2019-06-25T17:28:27Z[CET]"})
                print("device number ", device.id, " just sent some telemetry=", device.telemetry.metricValue)
                jsons = json.dumps(self.json_devices_telemetry)
                print("TELEMETry : ")
                print(self.json_devices_telemetry)
                return json.dumps(jsons)
        return None

    def Start(self, number_of_devices):
        print("START")
        self.devicePool.devices = self.deviceFactory.GenerateDevices(number_of_devices, self.macDomain)

        # First devices' update before listening for commands
        for device in self.devicePool.devices:
            self.deviceFactory.UpdateDeviceData(device) # Update device data

        self.ListenToReceiveCommand() # Devices are now listening for commands

        print("END")


    def Simulate(self):
        for device in self.devicePool.devices:
            self.deviceFactory.UpdateDeviceData(device)

        # TODO: Send telemetry to Java through RabbitMQ
        self.SendTelemetry()

    def SendTelemetry(self):
        j =  self.GetDevicesTelemetryAsJson()
        if j != None:
            Send(RABBITMQ_ENDPOINT, QUEUE_NAME_TELEMETRY, j)
        pass


    def ListenToReceiveCommand(self):
        ListenToReceive(RABBITMQ_ENDPOINT, QUEUE_NAME_COMMAND)
        pass
