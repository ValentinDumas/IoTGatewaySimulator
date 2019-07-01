import random

class MacAddressGeneratorOptimized:
    def __init__(self):
        self.generated_mac_addresses = {} # {'AA:AA:AA': ''}
        # self.current_mac_address = ""

    def GenerateMacAddress(self):
        mac_range = [random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1), random.randrange(0, 255, 1)]
        mac_address_numbers = []

        for number in mac_range:
            mac_address_numbers.append(hex(number))

        mac_address = self.HexadecimalNumbersToHexadecimalWords(mac_address_numbers)

        if self.generated_mac_addresses[mac_address] != '':
            print("Mac address already exists !")
            self.GenerateMacAddress() # => Regenerate an other MAC address
        else:
            self.generated_mac_addresses[mac_address] = mac_address
            # self.current_mac_address = mac_address

        # return self.current_mac_address

    def HexadecimalNumbersToHexadecimalWords(self, hexadecimal_numbers):
        return ':'.join(['%02X' % int(number, 16) for number in hexadecimal_numbers])


class MacAddressGenerator:
    def __init__(self):
        self.range = [0, 0, 0, 0, 0, 0]
        self.generated_mac_addresses = []

    def GenerateMacAddress(self):
        mac_address_numbers = []

        for number in self.range:
            mac_address_numbers.append(hex(number))

        mac_address = self.HexadecimalNumbersToHexadecimalWords(mac_address_numbers)

        self.generated_mac_addresses.append(mac_address)

        self.IncrementRangeByOne()

        return mac_address

    def HexadecimalNumbersToHexadecimalWords(self, hexadecimal_numbers):
        return ':'.join(['%02X' % int(number, 16) for number in hexadecimal_numbers])

    def IncrementRangeByOne(self):
        # Add conditions for mac addresses !
        #
        # FF:FF:FF:FF:FF:FF 	Adresse broadcast
        # 01:00:0C:CC:CC:CC	    Cisco Discovery Protocol
        # 01:80:C2:00:00:00	    Spanning Tree Protocol
        # 33:33:xx:xx:xx:xx	    Adresses multicast IPv6
        # 01:00:5E:xx:xx:xx	    Adresses multicast IPv4
        # 00:00:0c:07:ac:xx	    Adresses HSRP
        # 00:00:5E:00:01:XX	    Adresses VRRP
        for index, number in reversed(list(enumerate(self.range))):  # loop over self.range in REVERSED order
            if (number >= 255) and (
                    index - 1 >= 0):  # the later condition protects against an 'ArrayOutOfBounds exception" -> if 255 and not the first index
                self.range[index] = 0
                continue
            else:
                self.range[index] += 1
                break


### GENERATOR 1
# mac_address_generator = MacAddressGenerator()
# print(mac_address_generator.range)
# NUMBER_OF_DEVICES = 86400
# mac_address_generator.GenerateMacAddresses(NUMBER_OF_DEVICES)
# for addr in mac_address_generator.generated_mac_addresses:
#     print(addr)
# print("-----------------------------")
# print(mac_address_generator.range)

### GENERATOR 2
# mag2 = MacAddressGenerator2()
# i = 0
# while(i < 86400):
#     mag2.GenerateMacAddress()
#     i += 1
# for addr in mag2.generated_mac_addresses:
#     print(addr)
# print("yooooo")
# mag2.GenerateMacAddress()
# print("finished")
