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

import datetime
import flet as ft
from modules.models.formatter import Formatter as FMT
from modules.models.clone_messenger import CloneMessenger as CM

from modules.gui.main_gui import gui_app
# 
# FILE_CONFIG_NAME: str = './modules/configs.json'
# config_manager = CoMa(FILE_CONFIG_NAME)
# c_manager = CopyDetectorManager(config_manager)
# r_manager = RepoClonerManager(config_manager)
# start_time = datetime.datetime.now()


# ?#########? Start Timer Config ##########
# message_manager = CM()
# time_manager = FMT()
# time_manager.crude_time = start_time
# ?#########? End Timer Config ##########

# message_manager.message = f"Elapsed Time: {time_manager.formatted_time_str}"
# message_manager.print_success_message()

if __name__ == '__main__':
    ft.app(target=gui_app)