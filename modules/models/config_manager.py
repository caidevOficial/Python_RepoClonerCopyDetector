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

class ConfigManager:
    """Represents the class in charge of init the configs of the script"""
    def __init__(self, file_path: str) -> None:
        self.__file_path = file_path
        self.__main_configs = dict()
        self.__open_file()
        self.__app_info = self.__main_configs["app_info"]
        self.__rc_configs = self.__main_configs["repo_cloner"]
        self.__cd_configs = self.__main_configs["copy_detector"]
    
    def __open_file(self):
        """
        It opens a file, reads it, and then loads the contents of the file into a variable
        """
        self.__main_configs = pd.read_json(self.__file_path, orient='records')
    
    @property
    def version(self) -> str:
        return self.__app_info["version"]
    
    @property
    def main_csv_file(self) -> str:
        return self.__app_info["main_filename"]
    
    @property
    def app_name(self) -> str:
        return self.__app_info["app_name"]
    
    @property
    def author(self) -> str:
        return self.__app_info["author"]

    @property
    def rc_config(self) -> dict:
        return self.__rc_configs
    
    @property
    def cd_config(self) -> dict:
        return self.__cd_configs
    
    @property
    def rc_df_config(self) -> dict:
        return self.__rc_configs['DataFrame']['Fields']
    
    @property
    def rc_files_config(self) -> dict:
        return self.__rc_configs['Files']
    
    @property
    def rc_API_config(self) -> dict:
        return self.__rc_configs['Github']
    
    
    
