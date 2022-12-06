# GNU General Public License V3
#
# Copyright (c) 2022 [FacuFalcone]
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
import pandas as pd

from modules.models.df_handler import DataFrameHandler as DfH
from modules.models.data_manager import DataManager as DM
from modules.models.dir_manager import DirectoryManager as DirM
from modules.models.formatter import Formatter as FMT
from modules.models.plot_manager import PlotManager as Plot
from modules.models.clone_messenger import CloneMessenger as CM

# ?######### Start Basic Configuration ##########
FILENAME: str = 'Github_Repositories.csv'
NAME: str = 'Github Repository Cloner'
VERSION: str = '[V2.2.1.11]'
AUTHOR: str = '[FacuFalcone - CaidevOficial]'
FILE_CONFIG_NAME: str = './modules/configs.json'
# ?######### End Basic Configuration ##########

def __directories_creation(dir_manager: DirM, json_dir_config: dict):
    dirs = [
        json_dir_config['Dir_Plots_img'], 
        json_dir_config['Dir_Cloned_Repos'], 
        json_dir_config['Dir_Statistics']
    ]
    for actual_dir in dirs:
        dir_manager.path_to_create = actual_dir
        dir_manager.create_dir_if_no_exist()

def __config_df(handler: DfH, json_configs: dict, json_dir_config: dict):
    # *# Reads the 'csv' File to get the dataframe
    df = pd.read_csv(FILENAME)
    
    # *# Sets the Main DF to the class to handle it
    handler.configs_json_values = json_configs
    handler.main_dataframe = handler.format_DF(df, json_configs)
    handler.configurate_DF(
        handler.configs_json_values['Course'], 
        json_dir_config['Dir_Statistics']
    )

def __print_messages(message_manager: CM, time_manager: FMT, plotter_manager: Plot):
    messages = [
        f"Elapsed Time: {time_manager.formatted_time_str}",
        f"Thanks for using {NAME} {VERSION} by {AUTHOR}! ♥",
        "Creating Pie Chart...",
        "Success! All task done. Press a key to close the app"
    ]
    
    for i_msg in range(len(messages)):
        message_manager.message = messages[i_msg]
        message_manager.print_success_message()
        if i_msg == 2:
            plotter_manager.create_pie_chart()

def repo_cloner():
    try:
        start_time = datetime.datetime.now()
    # ?#########? Start Initialization ##########
        JsonFile = pd.read_json(f"./{FILE_CONFIG_NAME}", orient='records')["repo_cloner"]
        JsonAPI = JsonFile['Github']
        JsonDFConfigs: dict = JsonFile['DataFrame']['Fields']
        JsonDirConfigs: dict = JsonFile['Files']
    # ?#########? End Initialization ############

    # ?#########? Start Objects Instances ##########
        df_handler = DfH()
        data_manager = DM()
        message_manager = CM()
        time_manager = FMT()
        plotter_manager = Plot()
        dir_manager = DirM()
    # ?#########? End Objects Instances ##########

    # ?#########? Start Directory Creation ##########
        __directories_creation(dir_manager, JsonDirConfigs)
    # ?#########? End Directory Creation ##########

    # ?#########? Start DataManager Configuration ##########
        data_manager.initial_config(NAME, VERSION, AUTHOR, JsonAPI, JsonDirConfigs['Dir_Cloned_Repos'])
    # ?#########? End DataManager Configuration ##########

    # ?#########? Start DataFrame Configuration ##########
        # *# Reads the 'csv' File to get the dataframe
        __config_df(df_handler, JsonDFConfigs, JsonDirConfigs)
    # ?#########? End DataFrame Configuration ##########

    # ?#########? Start Initialize DataManager ##########
        data_manager.clone_repositories(df_handler)
    # ?##########? End Initialize DataManager ###########

    # ?#########? Start PlotManager Configuration ##########
        plotter_manager.initialize(df_handler, 'Cloned Repositories', JsonDirConfigs['Dir_Plots_img'])

    # ?#########? Start Timer Config ##########
        time_manager.crude_time = start_time
    # ?#########? End Timer Config ##########

    # ?#########? Start Print Message ##########
        __print_messages(message_manager, time_manager, plotter_manager)
    # ?#########? End Print Message ##########
    except Exception as e:
        message_manager.message = f'Exception: {e.args}'
        message_manager.print_warning_message()
    # finally:
    #     _ = input()

# if __name__ == '__main__':
#     repo_cloner()
