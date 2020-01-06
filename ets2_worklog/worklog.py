import PySimpleGUI
import threading

from ets2.model import Model
from ets2.mqtt_handler import mqtt_thread_loop, GlobalState
from ets2_worklog.view import View
from ets2_worklog.model import WorkLog


def main():
    model: Model = Model()
    work_log: WorkLog = WorkLog(model)
    state: GlobalState = GlobalState()
    mqtt_reader_thread = threading.Thread(target=mqtt_thread_loop,
                                          args=(model, work_log, state))
    mqtt_reader_thread.start()

    PySimpleGUI.ChangeLookAndFeel('Dark')
    hmi = View(model=model, work_log=work_log)

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
