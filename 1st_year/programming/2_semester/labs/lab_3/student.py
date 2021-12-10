"""
Author: Maxym Koval (Group K-12)
"""
from errors import LoadCsvError
from subject import Subject


class Student:
    """
    This class represent a student with a possibility to update information about subjects he passed

            Attributes:
                    transcript_id (str): transcript number
                    group_id (str): student group
                    name (str): student name
                    surname (str): student surname
                    patronymic (str): student patronymic
                    rating (int): student rating (arithmetic mean of student mark)
                    doubts_count (int): number of subject that student didn't pass
                    excellent_count (int): number of subject that student passed "excellently"
    """
    def __init__(self, transcript_id, group_id=None, name=None, surname=None, patronymic=None):
        Student._check_init_params(transcript_id, group_id, name, surname, patronymic)

        self._transcript_id = transcript_id
        self._group_id = group_id
        self._name = name
        self._surname = surname
        self._patronymic = patronymic
        self._rating = 0
        self._mark_sum = 0
        self._doubts_count = 0
        self._excellent_count = 0
        self._subjects = []

    @staticmethod
    def _check_init_params(transcript_id, group_id, name, surname, patronymic):
        if group_id is not None:
            if len(transcript_id) != 6:
                raise LoadCsvError("The transcript number must be equal to 6.")
            if len(group_id) > 5:
                raise LoadCsvError("The group id cannot contain more than 5 characters.")
            if len(name) > 24:
                raise LoadCsvError("The name cannot contain more than 24 characters.")
            if len(surname) > 27:
                raise LoadCsvError("The surname cannot contain more than 27 characters.")
            if len(patronymic) > 20:
                raise LoadCsvError("The patronymic cannot contain more than 20 characters.")

    def update(self, subject_name, total_points, mark, exam_points):
        """
        Update information about the subject student passed

                Parameters:
                        subject_name (str): name of the subject
                        total_points (int): subject points (max - 100)
                        mark (int): subject mark (max - 5)
                        exam_points (int): subject exam points (max - 40)
        """
        if (subject := self.find(subject_name)) is None:
            subject = self.add(subject_name)
        self._excellent_count += (mark == 5)
        self._mark_sum += mark if mark > 1 else 2
        self._rating = self._mark_sum / len(self._subjects)
        self._doubts_count += subject.update(total_points, mark, exam_points)

    def find(self, subject_name):
        """
        Find a subject by subject name

                Parameters:
                        subject_name (str): name of the subject

                Returns:
                        subjects(list): list of subjects
        """
        try:
            sub_index = self._subjects.index(Subject(subject_name))
            return self._subjects[sub_index]
        except ValueError:
            return None

    def add(self, subject_name):
        """
        Add a subject by subject name

                Parameters:
                        subject_name (str): name of the subject

                Returns:
                        subject(Subject): subject that was added
        """
        self._subjects.append(Subject(subject_name))
        return self._subjects[-1]

    def subjects2output(self, stream):
        """
        Write information about subjects with a mark less than 5 into stream

                Parameters:
                        stream(stream): stream to write information to
        """
        self._subjects.sort(key=lambda subject: (subject.subject_name, subject.total_points))
        for subject in self._subjects:
            if subject.mark < 5:
                subj_info = f"\t{subject.subject_name}\t{subject.total_points}\t{subject.mark}\n"
                stream.write(subj_info)

    def __eq__(self, other):
        return self.transcript_id == other.transcript_id

    @property
    def transcript_id(self):
        return self._transcript_id

    @property
    def group_id(self):
        return self._group_id

    @property
    def name(self):
        return self._name

    @property
    def surname(self):
        return self._surname

    @property
    def patronymic(self):
        return self._patronymic

    @property
    def rating(self):
        return self._rating

    @property
    def doubts_count(self):
        return self._doubts_count

    @property
    def excellent_count(self):
        return self._excellent_count
