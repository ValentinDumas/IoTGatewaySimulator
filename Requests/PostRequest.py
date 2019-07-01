# importing the requests library
import requests
from requests.auth import HTTPBasicAuth

import json

from DeviceSimulator.Models.Device import Device

# TODO: send datetime.now() in CET !!! not UTC
# CET = central european time (cet = +1)
# utc = +0

from datetime import datetime


def PostRequest(_url, _data):
    headers={'Content-type':'application/json', 'Accept':'application/json'}
    post_response = requests.post(url=_url,json=_data,headers=headers)

    # sending post request and saving response as response object
    # post_response = requests.post(url=_url, data=_data)
    print("POST request result: %s" % post_response)
    return post_response.text

#
# # Simulate a Device
# device = Device("GG:GG:GG:GG:GG:GG", "TT:TT:TT:TT:TT:TT", "2", ip="")
#
# # defining the api-endpoint
# DEVICE_ENDPOINT_API = "http://localhost:2889/device"
#
# print(datetime.now())
#
# device_json = {
#     'id': device.id,
#     'name': device.name,
#     'deviceType': device.device_type,
#     'ip': device.ip,
#     'macAddress': device.mac_address,
#     'macDomain': str(device.mac_domain),
# }
# jsons = json.dumps(device_json)
#
# r = PostRequest(DEVICE_ENDPOINT_API, jsons)
#
# print(r)
