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

from modules.common.color import Color

class CloneMessenger:
    """[summary]
    Class to print messages in the console. \n
    Returns:
        class: [CloneMessenger]. \n
    """

    def __init__(self) -> None:
        # ?######? START ATTRIBUTES #######
        self.__message: str = ''
        # ?######? END ATTRIBUTES #######

    # ?######? START PROPERTIES #######

    @property
    def message(self) -> str:
        """[summary] \n
        Get the message of the class. \n
        Returns:
            str: Message of the class. \n
        """
        return self.__message

    @message.setter
    def message(self, message: str) -> None:
        """[summary] \n
        Sets the message of the class. \n
        Args:
            message (str): The message to be printed in the console. \n
        """
        self.__message = message

    # ?######? END PROPERTIES #######

    # ?###########? START METHODS ############

    def __generate_symbols(self) -> str:
        """[summary] \n
        Generates a string of symbols of the same length of the message of the class. \n
        Returns:
            str: String of symbols of the same length of the message of the class. \n
        """
        return ''.join(['#' for i in range(len(self.message))])

    def initialize_messenger(self, message: str) -> None:
        """[summary] \n
        Initializes the class with a message. \n
        Args:
            message (str): The message to be printed in the console. \n
        """
        self.message = message

    def print_message(self) -> None:
        """[summary] \n
        Creates a string of symbols of the same length of the message and \n
        prints them in the console. \n
        like: \n
        ############### \n
        ##Your Message ## \n
        ############### \n
        """
        symbols = self.__generate_symbols()
        print(
            '\n',
            f'{symbols}',
            f'{self.message}',
            f'{symbols}',
            sep='\n'
        )
    
    def print_warning_message(self) -> None:
        """
        It prints a warning message in red and white
        """
        print(f'{Color._B_RED.value}{Color._F_WHITE.value}')
        self.print_message()
        print(f'{Color._NO_COLOR.value}')
    
    def print_success_message(self) -> None:
        print(f'{Color._B_BLUE.value}{Color._F_WHITE.value}')
        self.print_message()
        print(f'{Color._NO_COLOR.value}')

    # ?###########? END METHODS ############
