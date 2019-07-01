#!/usr/bin/env python
import pika
import time
import json
import serial

messages = []

def ListenToReceive(host, queue_name):
    ser = serial.Serial('COM4', 9600, timeout = 1)
    time.sleep(3) # Arduino initializing...

    connection = pika.BlockingConnection(
    pika.ConnectionParameters(host=host))
    channel = connection.channel()

    channel.queue_declare(queue=queue_name, durable=True)
    print(' [*] Waiting for messages. To exit press CTRL+C')
    messages.append("A")

    def callback(ch, method, properties, body):
        print("Message received: %r" % body)

        body = body.decode()
        m = body.split(';')

        if(len(m) == 2):

            deviceId = m[0]
            com = m[1]

            print("Device (ID = ", deviceId, " received the command '", com,"'")

            if(com == "led_on"):
                ser.write(b'H')
            elif(com == "led_off"):
                ser.write(b'L')
            elif(com == "beep"):
                ser.write(b'B')
            else:
                print("Message type unknown...")

        print(" [x] Done")
        ch.basic_ack(delivery_tag=method.delivery_tag)

    channel.basic_qos(prefetch_count=1)
    channel.basic_consume(queue=queue_name, on_message_callback=callback)

    channel.start_consuming()


ListenToReceive("localhost", "command_queue")

# messages.append("A")
# messages.append("B")
# messages.append("C")
#
# messages.pop()
#
# print(messages)
# print(str(len(messages)))

