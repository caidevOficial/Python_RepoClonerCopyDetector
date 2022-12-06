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

import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
from modules.models.df_handler import DataFrameHandler


class PlotManager:
    """[summary]
    Class in charge of create the pie chart. \n
    Returns:
        class: PlotManager
    """

    def __init__(self) -> None:
        # ?#### START ATTRIBUTES ####?
        self.__plotDF: DataFrameHandler = None
        self.__labels: list = []
        self.__slices: list = []
        self.__colors: list = []
        self.__title: str = None
        self.__pathToSave: str = None
        # ?#### END ATTRIBUTES ####?

    # ?### START PROPERTIES - GETTERS ###?
    
    @property
    def path_to_save(self) -> str:
        """[summary]
        Gets the path to save the image of the pie chart. \n
        Returns:
            str: [The path of the directory to save the image of the pie chart.]
        """
        return self.__pathToSave

    @property
    def labels(self) -> list:
        """[summary]
        Gets the list of labels for the pie chart. \n
        Returns:
            list: [Labels for the pie Chart]
        """
        return self.__labels

    @property
    def slices(self) -> list:
        """[summary]
        Gets the list of slices with values for every label \n
        of the pie chart. \n
        Returns:
            list: [Slices with values for using in the pie chart]
        """
        return self.__slices

    @property
    def plot_DF(self) -> DataFrameHandler:
        """[summary]
        Gets the DataFrameHandler object. \n
        Returns:
            class: DataFrameHandler
        """
        return self.__plotDF

    @property
    def colors(self) -> list:
        """[summary]
        Gets the list of colors for the pie chart. \n
        Returns:
            list: [Colors for the pie Chart]
        """
        return self.__colors
    
    @property
    def title(self) -> str:
        """[summary]
        Gets the title for the legend of the pie chart. \n
        Returns:
            str: [Title for the legend of the pie chart]
        """
        return self.__title

    # ?### END PROPERTIES - GETTERS ###?

    # ?### START PROPERTIES - SETTERS ###?

    @path_to_save.setter
    def path_to_save(self, path: str):
        """[summary]
        Sets the path to save the image of the pie chart. \n
        Args:
            path (str): [The path of the directory to save the image of the pie chart.]
        """
        self.__pathToSave = path.strip()

    @labels.setter
    def labels(self, value: list):
        """[summary]
        Sets the list of labels for the pie chart. \n
        Args:
            value (list): [Labels for using in the pie Chart]
        """
        self.__labels = value

    @slices.setter
    def slices(self, value: list):
        """[summary]
        Sets the list of slices with values for every label \n
        of the pie chart. \n
        Args:
            value (list): [Slices with values for using in the pie chart]
        """
        self.__slices = value
    
    @plot_DF.setter
    def plot_DF(self, value: DataFrameHandler):
        """[summary]
        Sets the DataFrameHandler object. \n
        Args:
            value (DataFrameHandler): [DataFrameHandler object]
        """
        self.__plotDF = value
    
    @colors.setter
    def colors(self, value: list):
        """[summary]
        Sets the list of colors for the pie chart. \n
        Args:
            value (list): [Colors for the pie Chart]
        """
        self.__colors = value

    @title.setter
    def title(self, value: str):
        """[summary]
        Sets the title for the legend of the pie chart. \n
        Args:
            value (str): [Title for the legend of the pie chart]
        """
        self.__title = value.strip()
    
    # ?### END PROPERTIES - SETTERS ###?

    # ?### START METHODS ###?

    def initialize(self, df: DataFrameHandler, title: str, path: str) -> None:
        """[summary]
        Initializes the PlotManager object. \n
        Args:
            df (DataFrameHandler): [DataFrameHandler object] \n
            title (str): [Title for the legend of the pie chart] \n
            path (str): [Path to save the image of the pie chart]
        """
        self.plot_DF = df
        self.labels = self.plot_DF.unique_columns
        self.slices = [len(dframe.index) for dframe in self.plot_DF.order_list_of_DF_students]
        self.title = title
        self.path_to_save = path

    def configure_rc_params(self) ->None:
        """[summary]
        Configures the rcParams of the matplotlib. \n
        """
        plt.style.use('seaborn-whitegrid')
        plt.rcParams['font.family'] = 'Times New Roman'
        plt.rcParams['font.size'] = 12
        plt.rcParams['legend.fontsize'] = 8
        plt.rcParams['lines.linewidth'] = 1.5
        plt.rcParams['lines.markersize'] = 5
        plt.rcParams['lines.markeredgewidth'] = 1
        plt.rcParams['figure.figsize'] = (12, 6)

    def create_pie_chart(self):
        """[summary]
        Creates the pie chart. \n
        """
        self.configure_rc_params()

        plt.pie(self.slices, labels=self.labels, startangle=45, shadow=True,
            autopct='%1.1f%%')
        plt.legend(self.labels, bbox_to_anchor=(1, 0.5), markerscale=1.2, loc='upper left')
        plt.title(self.title)
        plt.tight_layout()
        plt.savefig(f'{self.path_to_save}/{datetime.datetime.today().strftime("%Y%m%d__%H_%M_%S")}.png', dpi=300)
        plt.show()
