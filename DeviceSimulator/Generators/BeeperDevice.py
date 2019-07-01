import winsound
from datetime import datetime

class BeepConfig:
    def __init__(self):
        self.frequency = 442  # Set Frequency To 2500 Hertz
        self.duration = 1000  # Set Duration To 1000 ms == 1 second

class BeeperDevice:
    def __init__(self, device_mac_address = ""):
        self.device_mac_address = device_mac_address
        self.beep_config = BeepConfig()
        self.beep_command = "none"

    def Bind(self, device_mac_address):
        self.device_mac_address = device_mac_address

    def TriggerCommand(self):
        if self.beep_command == "beep":
            print("Playing beep on device ", self.device_mac_address, " for ", self.beep_config.duration, "ms")
            winsound.Beep(self.beep_config.frequency, self.beep_config.duration)
        else:
            print("[Error] Invalid command received for Beeper on device ", self.device_mac_address)

    def GetData(self):
        return self.beep_command, datetime.now()


# beeperDevice = BeeperDevice()
# beeperDevice.TriggerCommand()
#
# # ea.body
# body = "beep"
# beeperDevice.beep_command = body
# beeperDevice.TriggerCommand()
