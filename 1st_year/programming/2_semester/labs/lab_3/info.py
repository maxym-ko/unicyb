"""
Author: Maxym Koval (Group K-12)
"""

import sys

from student import Student
from errors import LoadCsvError, OutputError


class Information:
    """
    This class contains a list of students and some additional information about them

            Attributes:
                    mark_sum (int): marks sum
                    excellent_count (int): number of "excellent" marks
    """
    def __init__(self):
        self._students = []
        self._mark_sum = 0
        self._excellent_count = 0

    def load(self, transcript_id, group_id, name, surname, patronymic, subject_name, total_points, mark, exam_points):
        """
        Load information about the student and subject

                Parameters:
                        transcript_id (str): transcript number
                        group_id (str): student group
                        name (str): student name
                        surname (str): student surname
                        patronymic (str): student patronymic
                        subject_name (str): name of the subject
                        total_points (int): subject points (max - 100)
                        mark (int): subject mark (max - 5)
                        exam_points (int): subject exam points (max - 40)
        """
        if (student := self.find(transcript_id)) is None:
            student = self.add(transcript_id, group_id, name, surname, patronymic)
        elif not (
                student.group_id == group_id and student.name == name and student.surname == surname and student.patronymic == patronymic):
            raise LoadCsvError("Inconsistent information in .csv file.")
        self._excellent_count += mark == 5
        self._mark_sum += mark
        student.update(subject_name, total_points, mark, exam_points)

    def find(self, transcript_id):
        """
        Find a subject by subject name

                Parameters:
                        transcript_id (str): transcript number

                Returns:
                        students(list): list of students
        """
        try:
            st_index = self._students.index(Student(transcript_id))
            return self._students[st_index]
        except ValueError:
            return None

    def add(self, transcript_id, group_id, name, surname, patronymic):
        """
        Add a student by transcript number

                Parameters:
                        transcript_id (str): transcript number
                        group_id (str): student group
                        name (str): student name
                        surname (str): student surname
                        patronymic (str): student patronymic

                Returns:
                        student(Student): student that was added
        """
        self._students.append(Student(transcript_id, group_id, name, surname, patronymic))
        return self._students[-1]

    def output(self, filename, encoding):
        try:
            if not filename:
                self._output(sys.stdout)
            else:
                with open(filename, "w", encoding=encoding) as stream:
                    self._output(stream)
        except OSError:
            raise OutputError("Cannot output the result.")

    def _output(self, stream):
        self._students.sort(key=lambda student: (
            student.excellent_count, -student.doubts_count, student.surname, student.transcript_id))
        for student in self._students:
            if student.doubts_count and student.excellent_count:
                stream.write(f"{student.excellent_count}\t{student.doubts_count}\t{student.name}\t{student.surname}\t"
                             f"{student.rating}\t{student.transcript_id}\n")
                student.subjects2output(stream)

    def clear(self):
        """
        Clear all the information in the object
        """
        self._students.clear()
        self._mark_sum = 0
        self._excellent_count = 0

    def __enter__(self):
        self.clear()

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            self.clear()

    @property
    def mark_sum(self):
        return self._mark_sum

    @property
    def excellent_count(self):
        return self._excellent_count
