from DeviceSimulator.Models import Telemetry


class Device:
    def __init__(self, mac_domain, mac_address, device_type, ip=""):
        self.id = ""
        self.name = ""
        self.device_type = device_type
        self.ip = ip
        self.mac_domain = mac_domain
        self.mac_address = mac_address

        self.telemetry = Telemetry.Telemetry(None, None)

        self.command_device = None
        self.sensor_device = None
