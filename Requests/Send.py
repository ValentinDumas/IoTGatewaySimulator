#!/usr/bin/env python
import pika

# Can send telemetry like this
def Send(host, queue_name, message):
    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True, exclusive=False, auto_delete=False)

    body = message
    channel.basic_publish(
        exchange='',
        routing_key=queue_name,
        body=body,
        properties=pika.BasicProperties())
    print(" [x] Sent %r" % body)
    connection.close()


# 86400 Devices / 10 Gateways => 8640 Devices/Gateway

from datetime import datetime
from DeviceSimulator.Models.Telemetry import Telemetry

# t = Telemetry(str(datetime.now()), 64)
# json_device = {"id_device": 6, "value": t.metricValue, "date": "2019-06-25T17:28:27Z[CET]"}
# json_device = json.dumps(json_device)
# print(json_device)
