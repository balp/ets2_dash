
import paho.mqtt.client as mqtt
import PySimpleGUI
import json
import typing
import decimal

from ets2_dash.model import Model
from ets2_dash.view import View


model: Model = Model()


def on_message(client : typing.Any, userdata : typing.Any , message : object):
    # print("message received ", message.payload)
    # print("message topic=",message.topic)
    json_data = json.loads(message.payload)
    if message.topic == "ets2/data":
        model.set_telematic_data(json_data)
    if message.topic == "ets2/game":
        model.set_game(json_data)
    if message.topic == "ets2/info":
        model.set_info(json_data)
    elif message.topic == "ets2/info/config/job":
        model.set_job_config(json_data)



def main():
    print("Startup!!!")

    client = mqtt.Client("ets2_gui") #create new instance
    client.on_message = on_message
    client.connect("localhost") #connect to broker
    client.subscribe("ets2/data")
    client.subscribe("ets2/game")
    client.subscribe("ets2/info")
    client.subscribe("ets2/info/config/job")

    # client.subscribe("ets2/info/config/substances")
    # client.subscribe("ets2/info/config/controls")
    # client.subscribe("ets2/info/config/hshifter")
    # client.subscribe("ets2/info/config/truck")
    # client.subscribe("ets2/info/config/trailer")

    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(model)

    print("Loop!!!")
    while (True):
        # This is the code that reads and updates your window
        button, values = hmi.window.Read(timeout=100)
        # print("Loop data", myData.data)
        hmi.update_data()
        if button == 'Exit':
            break

        # Your code begins here
        client.loop(timeout=0.01, max_packets=1)


    # Broke out of main loop. Close the window.
    hmi.window.CloseNonBlockingForm()


if __name__ == '__main__':
    main()