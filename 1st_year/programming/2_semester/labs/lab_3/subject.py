"""
Author: Maxym Koval (Group K-12)
"""

from errors import LoadCsvError


class Subject:
    """
    This class represent a subject with a possibility to update information about points and mark

            Attributes:
                    subject_name (str): name of the subject
                    total_points (int): subject points (max - 100)
                    mark (int): subject mark (max - 5)
                    exam_points (int): subject exam points (max - 40)
    """
    def __init__(self, subject_name):
        Subject._check_subject_name(subject_name)

        self._subject_name = subject_name
        self._total_points = 0
        self._mark = 0
        self._exam_points = 0

    @staticmethod
    def _check_subject_name(subject_name):
        if len(subject_name) > 53:
            raise LoadCsvError("The subject name cannot contain more than 53 characters.")

    @staticmethod
    def _check_points(total_points, mark, exam_points):
        Subject._check_points_type(total_points, mark, exam_points)
        semester_points = total_points - exam_points
        if not (0 <= mark <= 5):
            raise LoadCsvError("The subject mark cannot be out of range (0, 5).")
        if not (0 <= semester_points <= 60):
            raise LoadCsvError("The number of subject semester points cannot be out of range (0, 60).")
        if not (24 <= exam_points <= 40):
            if exam_points == 0 and mark > 2:
                raise LoadCsvError("The subject mark cannot be higher than 2 when the subject exam points equal to 0.")
            else:
                raise LoadCsvError("The number of subject exam points cannot be out of range (24, 40) "
                                   "or not be equal to 0.")
        mark_correct = Subject._convert_points2mark(total_points)
        if mark not in mark_correct:
            raise LoadCsvError("The number of subject points and subject mark match each other.")

    @staticmethod
    def _check_points_type(total_points, mark, exam_points):
        try:
            int(total_points)
            int(mark)
            int(exam_points)
        except ValueError:
            raise LoadCsvError("The subject mark, total points, and exam points must be an integer.")

    @staticmethod
    def _convert_points2mark(total_points):
        if total_points < 60:
            return -1, 0, 2
        elif total_points < 75:
            return 3,
        elif total_points < 90:
            return 4,
        else:
            return 5,

    def update(self, total_points, mark, exam_points):
        """
        Update information about the subject points, mark and exam points

                Parameters:
                        total_points (int): subject points (max - 100)
                        mark (int): subject mark (max - 5)
                        exam_points (int): subject exam points (max - 40)
        """
        Subject._check_points(total_points, mark, exam_points)

        self._total_points = total_points
        self._mark = mark
        self._exam_points = exam_points
        return self.mark < 3

    def __eq__(self, other):
        return self.subject_name == other.subject_name

    @property
    def subject_name(self):
        return self._subject_name

    @property
    def total_points(self):
        return self._total_points

    @property
    def mark(self):
        return self._mark

    @property
    def exam_points(self):
        return self._exam_points
