"""
Author: Maxym Koval (Group K-12)
"""

import sys
import json
from loader import load
from info import Information
from errors import *


def print_author_info():
    about_author = "Author: Koval\n\tMaxym\nGroup:  K-12\n"
    print(about_author)


def print_task():
    task = "This is a laboratory work №3, Variant 69. Description of the program:\n\nThe program processes two files " \
           "- 1) main (.csv) and 2) additional (.json)\n1) The main file contains the following information about " \
           "the student: \n\t-name, \n\t-group id, \n\t-transcript number, \n\t-subject name, \n\t-points scored " \
           "during the semester, \n\t-points scored on the exam, \n\t-the total a 100-point system, \n\t-assessment " \
           "by the state form.\n2) The additional file contains the following information about the student: " \
           "\n\t-number of grades 'excellent', \n\t-the sum of the assessments of the student.\nAccording to these " \
           "files, the program finds students who did not pass some subjects but received an 'excellent' grade.\nThe " \
           "program output to console or in the file (the user chooses) the following information about these " \
           "students: the number of 'excellent' grades, the number of 'doubts', name, surname, rating, transcript " \
           "number.\nThe program also output the following information about the subjects that the student passed " \
           "'excellently': the name of the subject, the total score in points, the assessments.\n"
    print(task)


def print_start_program_help():
    help_info = "\nThe console command must contain only one argument." \
                "\n\nFollow the instructions below to avoid problem. \n" \
                "To run the program you should type the next line: \n" \
                "\t'python3.8 main.py params.json' \nor\n\t'main.py params.json'.\n\n"
    print(help_info)


def print_params_help():
    help_info = "\nCannot load the configuration .json file file." \
                "\n\nFollow the instructions below to avoid problems. \n" \
                "The settings .json file must contain dictionary with the keys 'input' and 'output'.\n" \
                "The value corresponding to\n" \
                "\t-the 'input' key is a dictionary with keys: 'csv', 'json', 'encoding'\n" \
                "\t-the 'output' key is a dictionary with keys: 'fname', 'encoding'\n\n"
    print(help_info)


def main(init_filename):
    """
    Perform all the work

                Parameters:
                        init_filename (str): configuration file name
    """
    try:
        print("ini " + init_filename + ": ", end="")
        ini_dict = load_ini(init_filename)
        print("OK")

        ini_input_dict = ini_dict["input"]
        ini_output_dict = ini_dict["output"]

        encoding_input = ini_input_dict["encoding"]
        filename_csv = ini_input_dict["csv"]
        filename_json = ini_input_dict["json"]
        encoding_output = ini_output_dict["encoding"]
        filename_output = ini_output_dict["fname"]

        information = Information()

        load(information, filename_csv, filename_json, encoding_input)

        if not filename_output:
            print("output stdout:", end="\n")
        else:
            print("output " + filename_output + ": ", end="")
        information.output(filename_output, encoding_output)
        if filename_output:
            print("OK")
    except InitError as e:
        print("\n", repr(e), sep="")
        print_params_help()
    except (ReadCsvError, LoadCsvError, ReadJsonError, LoadJsonError, ConsistentError, OutputError) as e:
        print("\n", repr(e), sep="")


def load_ini(filename):
    """
    Check file for required data inside and load it into dictionary

            Parameters:
                    filename (str): configuration file name

            Returns:
                    ini_dict (dict): dictionary with loaded information into it
    """
    try:
        with open(filename) as f:
            ini_dict = json.load(f)

        ini_keys = ["input", "output"]
        ini_input_keys = ["encoding", "csv", "json"]
        ini_output_keys = ["encoding", "fname"]
        if all(k in ini_dict for k in ini_keys):
            input_dict = ini_dict[ini_keys[0]]
            output_dict = ini_dict[ini_keys[1]]
            if not all(k in input_dict for k in ini_input_keys) or not all(k in output_dict for k in ini_output_keys):
                raise InitError(f"There are no required keys in the {filename}.")
        else:
            raise InitError(f"There are no required keys in the {filename}.")
        return ini_dict
    except OSError:
        raise InitError(f"Cannot open or read {filename}.")


if __name__ == "__main__":
    print_author_info()
    print_task()
    print("*****")
    if len(sys.argv) != 2:
        print("***** program aborted *****", "***** command line error *****", sep="\n")
        print_start_program_help()
    else:
        main(sys.argv[1])
