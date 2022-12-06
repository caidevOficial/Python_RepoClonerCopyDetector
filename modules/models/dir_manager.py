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

import os


class DirectoryManager:
    """[summary]
    Class in charge of create directories. \n
    Returns:
        class: DirectoryManager
    """

    def __init__(self) ->None:
        # ?#### START ATTRIBUTES ####?
        self.__dirToCreate: str = ''
        # ?#### END ATTRIBUTES ####?

    @property
    def path_to_create(self)-> str:
        """[summary]
        Gets the path that need to create if not exist. \n
        Returns:
            str: [Path to create.]
        """
        return self.__dirToCreate
    
    @path_to_create.setter
    def path_to_create(self, path: str)->None:
        """[summary]
        Sets the directory that will create. \n
        Args:
            path (str): [Directory to create.]
        """
        self.__dirToCreate = path

    def create_dir_if_no_exist(self)->None:
        """[summary]
        Creates the directory if not exist. \n
        """
        if not os.path.exists(self.path_to_create):
            os.makedirs(self.path_to_create)
    
