"""
Author: Maxym Koval (Group K-12)
"""

import csv

from errors import ReadCsvError, LoadCsvError


class Builder:
    """
    This class can load, process data from the file and load this data into Information object

            Attributes:
                    information (Information): an Information object to load data to
                    filename (str): name of file (.csv extension needs) with main information
                    encoding (str): file encoding
    """
    def __init__(self, information, filename, encoding):
        self._information = information
        self._filename = filename
        self._encoding = encoding
        self._loaded = False
        self._line = ""
        self._transcript_id = ""
        self._group_id = ""
        self._name = ""
        self._surname = ""
        self._patronymic = ""
        self._subject_name = ""
        self._total_points = 0
        self._mark = 0
        self._exam_points = 0

    def load(self):
        """
        Load data from the main file with given encoding to the given Information object

                Returns:
                        information (information): Information object with loaded data
        """
        if self._loaded:
            return self.information
        try:
            with self.information, open(self.filename, encoding=self.encoding) as file:
                it = csv.reader(file, delimiter=';')
                next(it)
                for self._line in it:
                    if self._line:
                        self._process_current_line()
                        self.information.load(self._transcript_id, self._group_id, self._name, self._surname,
                                              self._patronymic, self._subject_name, self._total_points, self._mark,
                                              self._exam_points)
            self._loaded = True
            return self.information
        except OSError:
            raise ReadCsvError("Cannot open or read .csv file.")

    def _process_current_line(self):
        if len(self._line) != 0:
            if len(self._line) != 9:
                raise LoadCsvError("The .csv file contains an invalid number of fields.")
            else:
                self._transcript_id = self._line[0]
                self._mark = self._line[1]
                self._subject_name = self._line[2]
                self._patronymic = self._line[3]
                self._exam_points = self._line[4]
                self._surname = self._line[5]
                self._name = self._line[6]
                self._total_points = self._line[7]
                self._group_id = self._line[8]
                self._covert_variables()

    def _covert_variables(self):
        try:
            self._total_points = int(self._total_points)
            self._mark = int(self._mark)
            self._exam_points = int(self._exam_points)
        except ValueError:
            raise LoadCsvError("Some of the fields can't be converted in .csv file.")

    @property
    def information(self):
        return self._information

    @property
    def filename(self):
        return self._filename

    @property
    def encoding(self):
        return self._encoding

    @property
    def loaded(self):
        return self._loaded
