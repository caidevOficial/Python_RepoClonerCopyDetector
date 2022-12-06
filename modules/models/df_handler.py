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

from numpy import ndarray
from pandas import DataFrame

from modules.models.formatter import Formatter as FMT
from modules.models.config_manager import ConfigManager as CoMa


class DataFrameHandler:
    """[summary] \n
    Class in charge of configurate and handle all the dataframe operations. \n
    Returns:
        class: [DataFrameHandler]. \n
    """

    def __init__(self, config_manager: CoMa) -> None:
        # ?####? Attributes #####
        self.__commands = list()
        self.__unique_columns: ndarray = list()
        self.__main_df: DataFrame = DataFrame()
        self.__students_df = list()
        self.__ordered_list_of_df_students: list[DataFrame] = list[DataFrame]()
        self.__configs = config_manager
        self.__configs_json_values: dict = self.__configs.rc_df_config
        # ?####? End Attributes #####

    # ?####? PROPERTIES - Getters #####

    @property
    def order_list_of_DF_students(self) -> list:
        """[summary] \n
        Get the list of ordered dataframes. \n
        Returns:
            [list]: [The list of ordered dataframes]. \n
        """
        return self.__ordered_list_of_df_students

    @property
    def configs_json_values(self) -> dict:
        """[summary] \n
        Get the configs of the json. \n
        Returns:
            [dict]: [The configs of the json]. \n
        """
        return self.__configs_json_values

    @property
    def main_dataframe(self) -> DataFrame:
        """[summary] \n
        Get the main dataframe. \n
        Returns:
            [DataFrame]: [The main dataframe]. \n
        """
        return self.__main_df

    @property
    def unique_columns(self) -> ndarray:
        """[summary] \n
        Get the unique values of the column 'columnValue' [Division]. \n
        Returns:
            [ndarray]: [The unique values of the column 'columnValue' [Division]]. \n
        """
        return self.__unique_columns

    @property
    def commands(self) -> list:
        """[summary] \n
        Get the list of the commands. \n
        Returns:
            [list]: [The list of the commands]. \n
        """
        return self.__commands

    @property
    def students_DF(self) -> list:
        """[summary] \n
        Get the dataframe with the students. \n
        Returns:
            [DataFrame]: [The dataframe with the students]. \n
        """
        return self.__students_df

    # ?####? End PROPERTIES - GETTERS #####

    # ?####? PROPERTIES - Setters #####

    @order_list_of_DF_students.setter
    def order_list_of_DF_students(self, frame: DataFrame) -> None:
        """[summary] \n
        Set the list of ordered dataframes. \n
        Args:
            frame (DataFrame): [The ordered dataframes]. \n
        """
        self.__ordered_list_of_df_students.append(frame.reset_index(drop=True))

    # @configs_json_values.setter
    # def configs_json_values(self, value: dict) -> None:
    #     """[summary] \n
    #     Set the configs of the json. \n
    #     Args:
    #         value (dict): [The configs of the json]. \n
    #     """
    #     self.__configs_json_values = value

    @main_dataframe.setter
    def main_dataframe(self, frame: DataFrame):
        """[summary] \n
        Set the main dataframe. \n
        Args:
            frame (DataFrame): [The dataframe to set]. \n
        """
        self.__main_df = frame

    @unique_columns.setter
    def unique_columns(self, unique_columns: ndarray):
        """[summary] \n
        Set the unique values of the column 'columnValue' [Division]. \n
        Args:
            unique_columns (ndarray): [The unique values of the column 'columnValue' [Division]]. \n
        """
        self.__unique_columns = unique_columns

    @commands.setter
    def commands(self, command: str) -> None:
        """[summary] \n
        Sets a command inside the list of the commands. \n
        Args:
            command (str): [The command to add]. \n
        """
        self.__commands.append(command)

    @students_DF.setter
    def students_DF(self, frame: DataFrame) -> None:
        """[summary] \n
        Set the dataframe with the students. \n
        Args:
            frame (DataFrame): [The dataframe with the students]. \n
        """
        self.__students_df.append(frame)

    # ?####? End PROPERTIES - SETTERS #####

    # ?####? METHODS #####

    def format_DF(self, df: DataFrame) -> DataFrame:
        """[summary] \n
        Format the dataframe by:\n
            - Removing the extra spaces.\n
            - Capitalizing the first letter of each word of Name & Surname.\n
            - Removing the Duplicateds rows.\n
        Args:
            df (DataFrame): [The dataframe to format].\n
            JsonDFConfigs (dict): [The dictionary with the values of columns to capitalize].\n
        Returns:
            [DataFrame]: [The formatted dataframe].\n
        """
        formatter = FMT()
        df = df.applymap(lambda x: str(x).strip())
        # ?# Apply a Capitalise in every word from both columns
        df[self.configs_json_values['Name']] = df[self.configs_json_values['Name']].apply(lambda x: formatter.capitalize_words(x))
        df[self.configs_json_values['Surname']] = df[self.configs_json_values['Surname']].apply(lambda x: formatter.capitalize_words(x))
        # ?# Removes the duplicated fields to avoid errors
        df = df.drop_duplicates(keep='first', subset=[self.configs_json_values['GitLink']])
        return df

    def __order_indexed_DF_by(self, frame: DataFrame, first_field: str, second_field: str, third_field: str) -> DataFrame:
        """[summary] \n
        Order the dataframe by the specified fields. \n
        Args:
            frame (DataFrame): [The dataframe to order]. \n
            first_field (str): [The first field to order]. \n
            second_field (str): [The second field to order]. \n
            third_field (str): [The third field to order]. \n
        Returns:
            [DataFrame]: [The dataframe ordered by the three fields in the specified order]. \n
        """
        sorted_df = frame.sort_values(
            by=[first_field, second_field, third_field], ascending=[True, True, True])
        return sorted_df

    def __get_specific_students_DF(self, frame: DataFrame, column: str, value: str) -> DataFrame:
        """[summary] \n
        Get the students that have the specified index value in the specified column. \n
        The DataFrame MUST be indexed by the 'value' column. \n
        Args:
            frame (DataFrame): [The dataframe to filter]. \n
            column (str): [The column to filter]. \n
            value (str): [The value to filter]. \n
        Returns:
            [DataFrame]: [The dataframe with the filtered students \n
            ordered by Course, Surname & Name]. \n
        """
        specific_df: DataFrame = frame[frame[column] == value]
        ordered_data_frame: DataFrame = self.__order_indexed_DF_by(
            specific_df, self.configs_json_values['Course'],
            self.configs_json_values['Surname'],
            self.configs_json_values['Name']
        )
        return ordered_data_frame

    def __create_list_DF_students_by(self, frame: DataFrame, column: str, column_value: str):
        """[summary] \n
        Creates a list of the students that have the specified index \n
        value in the specified column. \n
        The DataFrame MUST be indexed by the 'value' column. \n
        Args:
            frame (DataFrame): [The dataframe to filter]. \n
            column (str): [The column to filter]. \n
            column_value (list): [The values to filter]. \n
        """
        self.order_list_of_DF_students = self.__get_specific_students_DF(
            frame, column, column_value)

    def __config_unique_values_in_column(self, column: str):
        """[summary] \n
        Get the unique values in the specified column and sort them in alphabetical order ASC. \n
        Args:
            column (str): [The column to filter]. \n
        Returns:
            [list]: [The unique values in the specified column]. \n
        """
        self.unique_columns = self.main_dataframe[column].unique()
        self.unique_columns.sort()

    def __create_json_of_DF(self, frame: DataFrame, dir_statistics: str, name: str):
        """[summary] \n
        Create a json file for the specified dataframe. \n
        Args:
            frame (DataFrame): [The dataframe to create the json file]. \n
            dir_statistics (str): [The directory to save the json file]. \n
            name (str): [The name of the json file]. \n
        """
        frame.to_json(f'{dir_statistics}/{name}.json', orient='records',
                   indent=4, force_ascii=True)

    def create_json_of_each_DF(self, dir_statistics: str):
        """[summary] \n
        Create a json file for every dataframe. \n
        Args:
            dir_statistics (str): [The directory to save the json files]. \n
        """
        for students_df in self.order_list_of_DF_students:
            name = students_df.at[students_df.index.values[0],
                            self.configs_json_values['Course']]
            filename: str = f'{name}'
            self.__create_json_of_DF(students_df, dir_statistics, filename)

    # ?####? End METHODS #####

    # *####* MAIN METHOD #####

    def configurate_DF(self) -> None:
        """[summary] \n
        Configurate the dataframe with the specified column value. \n
        Args:
            column_value (str): [The column value to configurate]. \n
            dir_statistics (str): [The directory to save the json files]. \n
        """

        # *# Gets the unique values of the column 'column_value' [Division]
        self.__config_unique_values_in_column(self.configs_json_values['Course'])
        # *# For each unique value of the column 'column_value' [Division]
        # *# Creates a list of dataframes with the students that have the
        # *# specified value in the column 'column_value' [Division]
        for unique in self.unique_columns:
            self.__create_list_DF_students_by(
                self.main_dataframe, self.configs_json_values['Course'], unique
            )
        self.create_json_of_each_DF(self.__configs.rc_files_config['Dir_Statistics'])

    # *####* END MAIN METHOD #####
