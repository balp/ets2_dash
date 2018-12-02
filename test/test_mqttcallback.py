
import ets2_dash
import ets2_dash.mqtt_client

import json

class Message:
    def __init__(self, topic : str, payload : str, qos : int, retain : bool):
        self.topic = topic
        self.payload = payload
        self.qos = qos
        self.retain = retain

def test_one():
    message = Message("<topic>", "<payload>", 0, False)

    ets2_dash.mqtt_client.on_message(client=None,
                                     userdata=None,
                                     message=message)


def test_data():
    config_job_message = Message("ets2/info/config/job", '{"cargo":"Fuel Tanker",'
                                              '"cargo.id":"fueltanker",'
                                              '"cargo.mass":10440.0,'
                                              '"delivery.time":222605,'
                                              '"destination.city":"Glasgow",'
                                              '"destination.city.id":"glasgow",'
                                              '"destination.company":"ITCC",'
                                              '"destination.company.id":"itcc",'
                                              '"income":16050,'
                                              '"source.city":"Liverpool",'
                                              '"source.city.id":"liverpool",'
                                              '"source.company":"NBFC",'
                                              '"source.company.id":"nbfc"}', 0, False)
    ets2_dash.mqtt_client.on_message(client=None,
                                     userdata=None,
                                     message=config_job_message)

    config_truck_message = Message("ets2/info/config/truck", '{"adblue.capacity":80.0,'
                                                '"adblue.warning.factor":0.15000000596046448,'
                                                '"battery.voltage.warning":22.0,'
                                                '"brake.air.pressure.emergency":34.79999923706055,'
                                                '"brake.air.pressure.warning":69.5999984741211,'
                                                '"brand":"Volvo",'
                                                '"brand_id":"volvo",'
                                                '"cabin.position":{"x":0.0,"y":1.288755178451538,"z":-1.4456745386123657},'
                                                '"differential.ratio":3.0899999141693115,'
                                                '"forward.ratio":1.0,'
                                                '"fuel.capacity":800.0,'
                                                '"fuel.warning.factor":0.15000000596046448,'
                                                '"gears.forward":14,'
                                                '"gears.reverse":4,'
                                                '"head.position":{"x":-0.7175154685974121,"y":1.4037144184112549,"z":-0.4483802318572998},'
                                                '"hook.position":{"x":0.0,"y":1.0,"z":2.2579550743103027},'
                                                '"id":"vehicle.volvo.fh16_2012",'
                                                '"name":"FH",'
                                                '"oil.pressure.warning":10.149999618530273,'
                                                '"retarder.steps":3,'
                                                '"reverse.ratio":-3.2200000286102295,'
                                                '"rpm.limit":2100.0,'
                                                '"water.temperature.warning":105.0,'
                                                '"wheel.liftable":false,'
                                                '"wheel.position":{"x":0.95169997215271,"y":0.5018318891525269,"z":1.868200659751892},'
                                                '"wheel.powered":true,'
                                                '"wheel.radius":0.5062511563301086,'
                                                '"wheel.simulated":true,'
                                                '"wheel.steerable":false,'
                                                '"wheels.count":8}', 0, False)
    ets2_dash.mqtt_client.on_message(client=None,
                                     userdata=None,
                                     message=config_truck_message)

    config_trailer_msg = Message("ets2/info/config/trailer",
                      '{"cargo.accessory.id":".def.vehicle.trailer_cargo.scs_container.container_t14_diesel",'
                      '"hook.position":{"x":0.0,"y":1.0,"z":-5.0657806396484375},'
                      '"id":"scs_flatbed.flat_cont_gx2esii",'
                      '"wheel.liftable":true,'
                      '"wheel.position":{"x":0.8199999928474426,"y":0.5120000243186951,"z":1.5416467189788818},'
                      '"wheel.powered":false,'
                      '"wheel.radius":0.4977928102016449,'
                      '"wheel.simulated":true,'
                      '"wheel.steerable":false,'
                      '"wheels.count":6}', 0, False)
    ets2_dash.mqtt_client.on_message(client=None,
                                     userdata=None,
                                     message=config_trailer_msg)

def test_json_data():
    with open("data/telematic.json", "r") as j:
        telematic_data = json.load(j)
        message = Message("ets2/data", json.dumps(telematic_data), 0, False)
        ets2_dash.mqtt_client.on_message(client=None,
                                         userdata=None,
                                         message=message)