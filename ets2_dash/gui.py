
import PySimpleGUI
import threading
from dataclasses import dataclass

from ets2.model import Model
from ets2.mqtt_handler import mqtt_thread_loop
from ets2_dash.view import View


@dataclass
class GlobalState:
    active: bool = True


def main():
    print("Startup!!!")
    model: Model = Model()
    state: GlobalState = GlobalState()
    mqtt_reader_thread = threading.Thread(target=mqtt_thread_loop,
                                          args=(model, None, state))
    mqtt_reader_thread.start()

    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(model)

    print("Loop!!!")
    while True:
        event, values = hmi.window.Read(timeout=50)
        hmi.update_data()
        if event == 'Exit':
            break
    state.active = False
    mqtt_reader_thread.join(timeout=2.0)
    hmi.window.CloseNonBlockingForm()


if __name__ == '__main__':
    main()
