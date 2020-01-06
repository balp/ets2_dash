
import paho.mqtt.client as mqtt
import PySimpleGUI
import json
import typing
import logging
import threading
from dataclasses import dataclass

from ets2_dash.model import Model
from ets2_dash.view import View

@dataclass
class GlobalState:
    active: bool = True


def on_message(client: typing.Any, userdata: typing.Any , message : object):
    # print("message received ", message.payload)
    # print("message topic=",message.topic)
    assert isinstance(userdata, Model)
    model = userdata
    json_data = json.loads(message.payload)
    if message.topic == "ets2/data":
        model.set_telematic_data(json_data)
    elif message.topic == "ets2/game":
        model.set_game(json_data)
    elif message.topic == "ets2/info":
        model.set_info(json_data)
    elif message.topic == "ets2/info/config/job":
        model.set_job_config(json_data)
    elif message.topic == "ets2/info/config/truck":
        model.set_truck_config(json_data)
    elif message.topic == "ets2/info/config/trailer.0":
        model.set_trailer_config(json_data, 0)
    elif message.topic == "ets2/info/config/trailer.1":
        model.set_trailer_config(json_data, 1)
    elif message.topic == "ets2/info/config/trailer.2":
        model.set_trailer_config(json_data, 2)
    elif message.topic == "ets2/info/config/trailer.3":
        model.set_trailer_config(json_data, 3)
    elif message.topic == "ets2/info/config/trailer.4":
        model.set_trailer_config(json_data, 4)
    elif message.topic == "ets2/info/config/trailer.5":
        model.set_trailer_config(json_data, 5)
    elif message.topic == "ets2/info/config/trailer.6":
        model.set_trailer_config(json_data, 6)
    elif message.topic == "ets2/info/config/trailer.7":
        model.set_trailer_config(json_data, 7)
    elif message.topic == "ets2/info/config/trailer.8":
        model.set_trailer_config(json_data, 8)
    elif message.topic == "ets2/info/config/trailer.9":
        model.set_trailer_config(json_data, 9)


def mqtt_thread_loop(model: Model, state: GlobalState):
    client = mqtt.Client("ets2_gui", userdata=model) #create new instance
    client.on_message = on_message
    client.connect("localhost") #connect to broker
    client.subscribe("ets2/data")
    client.subscribe("ets2/game")
    client.subscribe("ets2/info")
    client.subscribe("ets2/info/config/job")
    client.subscribe("ets2/info/config/substances")
    # client.subscribe("ets2/info/config/controls")
    # client.subscribe("ets2/info/config/hshifter")
    client.subscribe("ets2/info/config/truck")
    # client.subscribe("ets2/info/config/trailer")

    client.subscribe("ets2/info/config/trailer.0")
    client.subscribe("ets2/info/config/trailer.1")
    client.subscribe("ets2/info/config/trailer.2")
    client.subscribe("ets2/info/config/trailer.3")
    client.subscribe("ets2/info/config/trailer.4")
    client.subscribe("ets2/info/config/trailer.5")
    client.subscribe("ets2/info/config/trailer.6")
    client.subscribe("ets2/info/config/trailer.7")
    client.subscribe("ets2/info/config/trailer.8")
    client.subscribe("ets2/info/config/trailer.9")

    while state.active:
        client.loop(timeout=1.0)

def main():
    print("Startup!!!")
    model: Model = Model()
    state: GlobalState = GlobalState()
    mqtt_reader_thread = threading.Thread(target=mqtt_thread_loop, args=(model, state))
    mqtt_reader_thread.start()

    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(model)

    print("Loop!!!")
    while (True):
        event, values = hmi.window.Read(timeout=50)
        hmi.update_data()
        if event == 'Exit':
            break
    state.active = False
    mqtt_reader_thread.join(timeout=2.0)
    hmi.window.CloseNonBlockingForm()


if __name__ == '__main__':
    main()