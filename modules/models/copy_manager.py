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
from modules.models.file import File
from modules.models.group import Group
from modules.models.file_manager import FileManager

class CopyManager:
    """Represents the class CopyManager that is in charge of handle the creation of groups of files that have possible copies"""

    def __init__(self, analyze_path: str, files_manager: FileManager) -> None:
        """
        This function takes a path to a directory and creates a list of files to analyze and a list of
        groups analyzed
        
        :param analyze_path: The path to the directory that contains the files to be analyzed
        :type analyze_path: str
        """
        self.__analyze_path = analyze_path
        self.__files_to_analyze = list[File]()
        self.__groups_analyzed = list[Group]()
        self.__files_sufix = files_manager.files_sufix
        self.__excluded_files = files_manager.excluded_files
    
    @property
    def groups_analyzed(self) -> list[Group]:
        """
        This function takes a list of files and returns a list of groups
        :return: A list of groups
        """
        self.make_files_to_analyze()
        self.make_groups()
        return self.__groups_analyzed

    def __print_files_path(self) -> None:
        """
        This function prints the path of each file in the list of files to analyze
        """
        for file in self.__files_to_analyze:
            print(file.path)

    def make_files_to_analyze(self) -> None:
        """
        It walks through a directory and returns a list of files that end with .c and are not named specs.c
        or spec.c
        :return: A list of File objects.
        """
        directories = list[str](filter(lambda file: 'Repositories' in file[0], os.walk('.', topdown=False)))
        for sufix in self.__files_sufix:
            for index in directories:
                if index[2]:
                    files = list[str](filter(lambda file: str(file).endswith(sufix), index[2]))
                    if files:
                        for filename in files:
                            if not filename in self.__excluded_files:
                                file_path = os.path.join(index[0], filename)
                                file_stats = os.stat(file_path).st_size
                                self.__files_to_analyze.append(File(file_path, file_stats, filename))
            
        # for root, dirs, files in os.walk(self.__analyze_path, topdown=False):
        #     for name in files:
        #         if name.endswith(".c") and name != "specs.c" and name != "spec.c":
        #             file_path = os.path.join(root, name)
        #             file_stats = os.stat(file_path).st_size
        #             self.__files_to_analyze.append(File(file_path, file_stats, name))
        print(f"{len(self.__files_to_analyze)} files detected.")
        self.__print_files_path()

    def make_groups(self) -> list[Group]:
        """
        It takes a list of files and returns a list of groups of files
        
        :param files_to_analyze: list[str]
        :type files_to_analyze: list[str]
        :return: A list of groups.
        """
        flag_once = True
        for file in self.__files_to_analyze:
            if flag_once:
                flag_once = False  # solo entro la primera vez
                self.__groups_analyzed.append(Group(file))

            # pregunto si el archivo pertecene a los grupos
            flag_belong = False
            for group in self.__groups_analyzed:
                if group.file_belong(file):
                    # si pertecene a un grupo existente lo agrego
                    group.append_file(file)
                    flag_belong = True

            # si no pertenece a ninguno, lo agrego a uno nuevo
            if not flag_belong:
                self.__groups_analyzed.append(Group(file))
