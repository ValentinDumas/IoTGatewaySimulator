import random
import json
from Requests.PostRequest import PostRequest
from DeviceSimulator.Models.Device import Device
from DeviceSimulator.Generators import LEDDevice, BeeperDevice
from DeviceSimulator.Generators import AtmosphericPressureSensor, BrightnessSensor, CO2Sensor, GPSSensor, HumiditySensor, LEDDevice, PresenceSensor, SoundLevelSensor, TemperatureSensor
from DeviceSimulator.Generators.MacAddressGenerator import MacAddressGenerator, MacAddressGeneratorOptimized


DOTNET_PLATFORM_ENDPOINT = "http://localhost:2889/device" # url to call the "createDevice" method from the .NET Device Endpoint API
DEFAULT_DEVICE_IP = "0.0.0.0"


class DeviceFactory:
    def __init__(self, mac_address_generator):
        self.mac_address_generator = mac_address_generator
        self.possible_device_types = [
            "ledDevice",
            "beeperDevice",
            "presenceSensor",
            "temperatureSensor",
            "brightnessSensor",
            "atmosphericPressureSensor",
            "humiditySensor",
            "soundLevelSensor",
            "gpsSensor",
            "co2Sensor"
        ]


# TODO: Device type map <DeviceType(string) to 0,1,2,3,...>
    # Compile data as Json
    def GetDeviceAsJson(self, device):
        json_device = {
            "id": device.id,
            "name": device.name,
            "deviceType": 3,
            "ip": device.ip,
            "macAddress": device.mac_address,
            "macDomain": device.mac_domain
        }

        return json.dumps(json_device)


    def GetId(self, url, device):
        deviceAsJson = self.GetDeviceAsJson(device) # Converts device object to json
        device_id = PostRequest(url, deviceAsJson) # Get a unique ID for the created device
        print("A device got an id=", device_id)
        return device_id


    # TODO: see how and when to generate IP
    def CreateDevice(self, macDomain, url=DOTNET_PLATFORM_ENDPOINT, ip=DEFAULT_DEVICE_IP):
        device = Device(macDomain, self.mac_address_generator.GenerateMacAddress(), random.choices(self.possible_device_types)[0], ip)
        #device.id = self.GetId(url, device)
        self.BindSensorOrCommand(device)
        self.UpdateDeviceData(device)
        return device


    def UpdateDeviceData(self, device):
        if not (device.command_device == None):
            device.telemetry.metricValue, device.telemetry.metricDate = device.command_device.GetData()
        if not (device.sensor_device == None):
            device.telemetry.metricValue, device.telemetry.metricDate = device.sensor_device.GetData()


    def BindSensorOrCommand(self, device):
        # DEVICE WITH COMMAND
        if(device.device_type == "ledDevice"):
            device.command_device = LEDDevice.LEDDevice(device.mac_address)
        elif(device.device_type == "beeperDevice"):
            device.command_device = BeeperDevice.BeeperDevice(device.mac_address)

        # DEVICE WITH SENSOR
        if(device.device_type == "presenceSensor"):
            device.sensor_device = PresenceSensor.PresenceSensor()
        elif(device.device_type == "temperatureSensor"):
            device.sensor_device = TemperatureSensor.TemperatureSensor()
        elif(device.device_type == "brightnessSensor"):
            device.sensor_device = BrightnessSensor.BrightnessSensor()
        elif(device.device_type == "atmosphericPressureSensor"):
            device.sensor_device = AtmosphericPressureSensor.AtmosphericPressureSensor()
        elif(device.device_type == "humiditySensor"):
            device.sensor_device = HumiditySensor.HumiditySensor()
        elif(device.device_type == "soundLevelSensor"):
            device.sensor_device = SoundLevelSensor.SoundLevelSensor()
        elif(device.device_type == "gpsSensor"):
            device.sensor_device = GPSSensor.GPSSensor()
        elif(device.device_type == "co2Sensor"):
            device.sensor_device = CO2Sensor.C02Sensor()


    def GenerateDevices(self, number_of_devices, macDomain):
        devices = []
        i = 0

        while(i < number_of_devices):
            devices.append(self.CreateDevice(macDomain))
            i += 1

        return devices
