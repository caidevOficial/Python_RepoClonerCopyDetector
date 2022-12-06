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


class Formatter:
    """[summary] \n
    Formats the time saved in the attribute of the class, as a string. \n
    like: {:02.0f} minute(s) {:02.0f} seconds. \n
    Returns:
        class: [Formatter]. \n
    """

    def __init__(self) -> None:
        # ?###########? START ATTRIBUTES ############
        self.__crudeTime = None
        self.__formattedTimeStr: str = ''
        # ?###########? END ATTRIBUTES ############

    # ?######? START PROPERTIES #######

    @property
    def crude_time(self) -> datetime:
        return self.__crudeTime

    @property
    def formatted_time_str(self) -> str:
        """[summary] \n
        Gets the formatted time string.\n
        Returns:
            str: [The formatted time string.]\n
        """
        self.__format_datetime_as_string()
        return self.__formattedTimeStr

    @crude_time.setter
    def crude_time(self, value: datetime) -> None:
        """[summary] \n
        Sets the time into the class and format it as a string like: \n
        {:02.0f} minute(s) {:02.0f} seconds. \n
        Args:
            value (datetime): [Time to be formatted and saved into the class.]\n
        """
        self.__crudeTime = value

    @formatted_time_str.setter
    def formatted_time_str(self, formatTime: str) -> None:
        """[summary] \n
        Sets the formatted time as a string.\n
        Args:
            start_time (datetime): [Formatted Time]\n
        """
        self.__formattedTimeStr = formatTime

    # ?###########? END  PROPERTIES ############

    # ?###########? START METHODS ############

    def __format_datetime_as_string(self) -> None:
        """[summary] \n
        Formats the time saved in the attribute of the class, as a string. \n
        like: {:02.0f} minute(s) {:02.0f} seconds. \n
        """
        seconds = (datetime.datetime.now() - self.crude_time).total_seconds()
        m, s = divmod(seconds, 60)
        self.formatted_time_str = "{:02.0f} minute(s) {:02.0f} seconds".format(m, s)

    def capitalize_words(self, string: str) -> str:
        """[summary] \n
        Capitalize each word of the string. \n
        Args:
            string (str): [The string to be capitalized.]\n
        Returns:
            str: [Every word of the string capitalized.]\n
        """
        # return ' '.join(word.capitalize() for word in string.split(' '))
        return ' '.join(list[str](map(lambda x: str(x).capitalize(), string.split(' '))))

    # ?###########? END METHODS ############
