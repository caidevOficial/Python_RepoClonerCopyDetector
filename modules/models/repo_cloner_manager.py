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

import pandas as pd

from modules.models.df_handler import DataFrameHandler as DfH
from modules.models.data_manager import DataManager as DM
from modules.models.dir_manager import DirectoryManager as DirM
from modules.models.formatter import Formatter as FMT
from modules.models.plot_manager import PlotManager as Plot
from modules.models.clone_messenger import CloneMessenger as CM
from modules.models.config_manager import ConfigManager as CoMa

class RepoClonerManager:
    """Represents the class of the Repository Cloner Manager"""
    
    def __init__(self, config_manager: CoMa) -> None:
        self.__config_manager = config_manager

    def __directories_creation(self, dir_manager: DirM, config_manager: CoMa):
        """
        It creates directories if they don't exist
        
        :param dir_manager: DirM = DirManager()
        :type dir_manager: DirM
        :param config_manager: CoMa = CoMa()
        :type config_manager: CoMa
        """
        for _, path in config_manager.rc_files_config.items():
            dir_manager.path_to_create = path
            dir_manager.create_dir_if_no_exist()

    def __config_df(self, handler: DfH, config_manager: CoMa):
        """
        It reads the csv file and sets the main dataframe to the class to handle it
        
        :param handler: DfH = DfH()
        :type handler: DfH
        :param config_manager: CoMa = CoMa()
        :type config_manager: CoMa
        """
        # *# Reads the 'csv' File to get the dataframe
        df = pd.read_csv(config_manager.main_csv_file)
        
        # *# Sets the Main DF to the class to handle it
        handler.main_dataframe = handler.format_DF(df)
        handler.configurate_DF()

    def __print_messages(self, message_manager: CM, plotter_manager: Plot, config_manager: CoMa):
        """
        It prints a message, then creates a pie chart
        
        :param message_manager: CM
        :type message_manager: CM
        :param plotter_manager: Plot
        :type plotter_manager: Plot
        :param config_manager: CoMa = CoMa()
        :type config_manager: CoMa
        """
        messages = [
            f"Thanks for using {config_manager.app_name} {config_manager.version} by {config_manager.author}! ♥",
            "Creating Pie Chart..."]
        
        for i_msg in range(len(messages)):
            message_manager.message = messages[i_msg]
            message_manager.print_success_message()
            if i_msg == 1:
                plotter_manager.create_pie_chart()

    def start_cloning_repositories(self, event):
        """
        It clones the repositories from the dataframe in different directories
        
        :param configs_manager: CoMa
        :type configs_manager: CoMa
        """
        # ?#########? Start Objects Instances ##########
        data_manager = DM()
        message_manager = CM()
        plotter_manager = Plot()
        dir_manager = DirM()
        # ?#########? End Objects Instances ##########
        try:
        # ?#########? Start Objects Instances ##########
            df_handler = DfH(self.__config_manager)
        # ?#########? End Objects Instances ##########

        # ?#########? Start Directory Creation ##########
            self.__directories_creation(dir_manager, self.__config_manager)
        # ?#########? End Directory Creation ##########

        # ?#########? Start DataManager Configuration ##########
            data_manager.initial_config(self.__config_manager)
        # ?#########? End DataManager Configuration ##########

        # ?#########? Start DataFrame Configuration ##########
            # *# Reads the 'csv' File to get the dataframe
            self.__config_df(df_handler, self.__config_manager)
        # ?#########? End DataFrame Configuration ##########

        # ?#########? Start Initialize DataManager ##########
            data_manager.clone_repositories(df_handler)
        # ?##########? End Initialize DataManager ###########

        # ?#########? Start PlotManager Configuration ##########
            plotter_manager.initialize(df_handler, 'Cloned Repositories', self.__config_manager.rc_files_config['Dir_Plots_img'])

        # ?#########? Start Print Message ##########
            self.__print_messages(message_manager, plotter_manager, self.__config_manager)
        # ?#########? End Print Message ##########
        except Exception as e:
            message_manager.message = f'Exception: {e.args}'
            message_manager.print_warning_message()
