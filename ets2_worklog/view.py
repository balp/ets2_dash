
import ets2.model
import PySimpleGUI


class View:
    def __init__(self, model, work_log):
        self._data: ets2.model.Model = model
        self._work_log = work_log
        self._setup_window()
        self._count = 0

    def _setup_window(self):
        game_info = [PySimpleGUI.Text('',
                                      size=(70, 1),
                                      justification="center",
                                      key="game_name"),
                     PySimpleGUI.Text('',
                                      size=(20, 1),
                                      justification="left",
                                      key="game_pause")
                     ]
        table_layout = [
            PySimpleGUI.Table(values=[['' for row in range(5)]for col in range(6)])
        ]
        exit_button_layout = [
            PySimpleGUI.Exit(button_color=('white', 'firebrick4'))
        ]

        layout = [game_info,
                  table_layout,
                  exit_button_layout]

        self.window = PySimpleGUI.Window("ETS2 - Work Log").Layout(layout).Finalize()

    def _update_element(self, key: str, value: str):
        self.window.FindElement(key).Update(value)

    def update_data(self):
        self._update_element('game_name', self._data.get_game_name())
        self._update_element('game_pause', 'paused' if self._data.get_game_pause() else '')
