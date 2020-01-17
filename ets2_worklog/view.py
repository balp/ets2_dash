
import ets2.model
import PySimpleGUI

from ets2.work_log import game_time_to_datetime


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
            PySimpleGUI.Table(values=[['', '', '', '', '', '',
                                       '', '', '', '', '']],
                              headings=['Cargo', 'Mass', 'From City', 'From Company', 'To City', 'To Company',
                                        '    Start  ', '    End   ', 'Time', 'EIncome', 'AIncome'],
                              col_widths=[20, 5, 20, 20, 20,
                                          20, 10, 10, 5, 10,
                                          10],
                              key='job_table')
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

        jobs = []
        for job in self._work_log.jobs:
            cargo = ''
            mass = ''
            source_city = ''
            source_company = ''
            destination_city = ''
            destination_company = ''
            income_expect = ''

            if job.config is not None:
                cargo = job.config.cargo
                mass = job.config.cargo_mass
                source_city = job.config.source_city
                source_company = job.config.source_company
                destination_city = job.config.destination_city
                destination_company = job.config.destination_company
                income_expect = job.config.income

            started = ''
            if job.started is not None:
                started = game_time_to_datetime(job.started).strftime('%j %a %T')

            ended = ''
            if job.ended is not None:
                ended = game_time_to_datetime(job.ended).strftime('%j %a %T')

            time = ''
            income_actual = ''
            if job.delivered is not None:
                time = job.delivered.time
                income_actual = job.delivered.revenue

            info = [cargo, mass, source_city, source_company, destination_city, destination_company,
                    started, ended, time, income_expect, income_actual]
            jobs.append(info)
        self.window.FindElement('job_table').Update(jobs)
