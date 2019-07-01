from datetime import datetime

class LEDDevice:
    def __init__(self, device_mac_address = ""):
        self.device_mac_address = device_mac_address
        self.led_command = "led_off"

    def Bind(self, device_mac_address):
        self.device_mac_address = device_mac_address

    def TriggerCommand(self):
        if self.led_command == "led_on":
            print("Led switch: ON on device ", self.device_mac_address)
        elif self.led_command == "led_off":
            print("LED switch: OFF on device ", self.device_mac_address)
        else:
            print("[Error] Invalid command received for LED on device ", self.device_mac_address)

    def GetData(self):
        return self.led_command, datetime.now()
