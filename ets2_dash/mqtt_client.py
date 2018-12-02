import paho.mqtt.client as mqtt
import typing

def on_message(client : typing.Any, userdata : typing.Any, message : object):
    print("message received " , message.payload)
    print("message topic=",message.topic)
    print("message qos=",message.qos)
    print("message retain flag=",message.retain)

def main():
    client = mqtt.Client("ets2_dash") #create new instance
    client.on_message = on_message
    client.connect("localhost") #connect to broker
    client.subscribe("ets2/data")
    client.subscribe("ets2/info/config/substances")
    client.subscribe("ets2/info/config/job")
    client.subscribe("ets2/info/config/controls")
    client.subscribe("ets2/info/config/hshifter")
    client.subscribe("ets2/info/config/truck")
    client.subscribe("ets2/info/config/trailer")

    client.loop_forever()

if __name__ == '__main__':
    main()