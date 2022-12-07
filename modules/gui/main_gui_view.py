# GNU General Public License V3
#
# Copyright (C) <2022>  <Facundo Falcone>
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 3 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful,
# but WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
# GNU General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see <https://www.gnu.org/licenses/>.

import flet as ft
from modules.models.copy_detector_manager import CopyDetectorManager
from modules.models.repo_cloner_manager import RepoClonerManager
from modules.models.config_manager import ConfigManager as CoMa
from modules.database.db_manager import DAOManager

class MainView(ft.UserControl):

    def build(self):
        # ?######### Start Basic Configuration ##########
        FILE_CONFIG_NAME: str = './modules/configs.json'
        config_manager = CoMa(FILE_CONFIG_NAME)
        self.__c_manager = CopyDetectorManager(config_manager)
        self.__r_manager = RepoClonerManager(config_manager)
        self.__dao_manager = DAOManager(config_manager.cd_config)
        # ?######### End Basic Configuration ##########
        self.__console = ft.Column()
        self.__console_area = ft.Row(
            controls=[ft.Text(value='Aca abajo iria una consola pero bueno, pasaron cosas.'), self.__console], alignment=ft.MainAxisAlignment.CENTER
        )
        self.__btns_area = ft.Row(controls=[
                            ft.TextButton(
                                text='Clonar Repositorios', icon=ft.icons.DOWNLOAD_SHARP, 
                                on_click=self.__r_manager.start_cloning_repositories),
                            ft.TextButton(
                                text='Chequear Copias', icon=ft.icons.CHECK_SHARP, 
                                on_click=self.__c_manager.start_checking_copies),
                            ft.TextButton(
                                text='Ver Base de datos', icon=ft.icons.DATASET_SHARP,
                                on_click=self.show_data)
                    ], alignment=ft.MainAxisAlignment.CENTER)
        self.__view = ft.Column(width=600, controls=[self.__btns_area, self.__console_area], alignment=ft.MainAxisAlignment.CENTER)

        return self.__view
    
    def show_data(self, event):
        data: list[tuple] = self.__dao_manager.read_table()
        data_text = [ft.Text(t_data) for t_data in data]
        self.__console = ft.Column(width=600, controls=data_text, alignment=ft.MainAxisAlignment.CENTER)
        self.update()
