import json
import typing
from dataclasses import dataclass

from paho.mqtt import client as mqtt

from ets2.model import Model, add_json_to_model
from ets2_worklog.model import WorkLog, add_json_to_work_log


@dataclass
class GlobalState:
    active: bool = True


def on_message(client: typing.Any, userdata: typing.Any, message: typing.Any):
    """Handle a mqtt message and send to Model"""
    model, work_log = userdata
    assert isinstance(model, Model)
    json_data = json.loads(message.payload)
    add_json_to_model(model=model, json_data=json_data, topic=message.topic)
    if work_log is not None:
        assert isinstance(work_log, WorkLog)
        add_json_to_work_log(work_log=work_log, json_data=json_data,
                             topic=message.topic)


def mqtt_thread_loop(model: Model, work_log: WorkLog, state: GlobalState) -> None:
    client = mqtt.Client("ets2_gui", userdata=(model, work_log))
    client.on_message = on_message
    client.connect("localhost")
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

    client.subscribe("ets2/info/gameplay/job.cancelled")
    client.subscribe("ets2/info/gameplay/job.delivered")
    client.subscribe("ets2/info/gameplay/player.tollgate.paid")
    client.subscribe("ets2/info/gameplay/player.use.ferry")

    while state.active:
        client.loop(timeout=1.0)

