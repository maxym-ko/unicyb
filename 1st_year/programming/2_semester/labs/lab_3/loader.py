"""
Author: Maxym Koval (Group K-12)
"""

import json

from builder import Builder
from errors import ReadJsonError, LoadJsonError


def load(information, filename_csv, filename_json, encoding):
    """
    Load data from two files (filename_csv and filename_json) with given encoding to the given Information object

            Parameters:
                    information (Information): an Information object to load data to
                    filename_csv (str): name of file (.csv extension needs) with main information
                    filename_json (str): name of file (.json extension needs) with additional information
                    encoding (str): encoding of both files

            Returns:
                    (bool): success of execution
    """
    print("input-csv " + filename_csv + ": ", end="")
    load_data(information, filename_csv, encoding)
    print("OK")
    print("input-json " + filename_json + ": ", end="")
    stat_dict = load_stat(filename_json, encoding)
    print("OK")
    print("json?=csv: ", end="")
    fit(information, stat_dict)
    print("OK")
    return True


def load_data(information, filename, encoding):
    """
    Load data from the main file (filename) with given encoding to the given Information object

            Parameters:
                    information (Information): an Information object to load data to
                    filename (str): name of file (.csv extension needs)
                    encoding (str): file encoding
    """
    Builder(information, filename, encoding).load()


def load_stat(filename, encoding):
    """
        Load data from the additional file (filename) with given encoding to the given Information object

                Parameters:
                        filename (str): name of file (.json extension needs)
                        encoding (str): file encoding

                Returns:
                        stat_dict (dict): dictionary from file with modified keys
    """
    try:
        with open(filename, encoding=encoding) as f:
            stat_dict = json.load(f)
    except OSError:
        raise ReadJsonError(f"Cannot read(open) the {filename}.")
    stat_keys = ["кількість «відмінно»", "сума державних оцінок"]
    if not all(k in stat_dict for k in stat_keys):
        raise LoadJsonError(f"There are no required keys in the {filename}.")
    stat_dict["excellent_count"] = stat_dict.pop("кількість «відмінно»")
    stat_dict["mark_sum"] = stat_dict.pop("сума державних оцінок")
    return stat_dict


def fit(information, stat_dict):
    """
        Check if data in Information object (information) coincide the data in the dictionary (stat_dict)

                Parameters:
                        information (Information): an Information object to check
                        stat_dict (dict): dictionary with required keys

                Returns:
                        (bool): success of execution
    """
    if stat_dict["excellent_count"] != information.excellent_count and stat_dict["mark_sum"] != information.mark_sum:
        raise IndentationError("The information in the .csv and .json files doesn't fit.")
    return True
