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
from modules.models.formatter import Formatter as FMT
from modules.models.config_manager import ConfigManager as CoMa
from modules.models.clone_messenger import CloneMessenger as CM
from modules import c_manager, r_manager


if __name__ == '__main__':
    # ?######### Start Basic Configuration ##########
    FILE_CONFIG_NAME: str = './modules/configs.json'
    config_manager = CoMa(FILE_CONFIG_NAME)
    start_time = datetime.datetime.now()
    # ?######### End Basic Configuration ##########
    
    # ?#########? Start Timer Config ##########
    message_manager = CM()
    time_manager = FMT()
    time_manager.crude_time = start_time
    # ?#########? End Timer Config ##########
    
    r_manager(config_manager)
    c_manager(config_manager)

    message_manager.message = f"Elapsed Time: {time_manager.formatted_time_str}"
    message_manager.print_success_message()