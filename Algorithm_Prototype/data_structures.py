"""
    Module data structures is used to prepare data get from backend for algorithm.
"""
# pylint: disable=C0301, W0511, R1735, C0116, R0903, R0902
import string
from random import shuffle

CLASSES = {
    # zw = zwykła
    100: "zw",
    101: "zw",
    102: "zw",
    103: "zw",
    104: "zw",
    200: "wf"
}

CLASSES_REQ = {
    'wf'
}

TEACHERS = {
    "Janusz Walczuk": {
        'subject': ["matematyka"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Krystyna Pawłowicz": {
        'subject': ["j.polski"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Robert Lewandowski": {
        'subject': ["wf"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Waldemar Kiepski": {
        'subject': ["chemia"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Ksiądz Robak": {
        'subject': ["religia"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': None,
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': None
        }
    },
    "Snoop Dogg": {
        'subject': ["biologia"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Albert Einstein": {
        'subject': ["fizyka"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Morgan Freeman": {
        'subject': ["matematyka"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Juliusz Słowacki": {
        'subject': ["j.polski"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Arkadiusz Milik": {
        'subject': ["wf"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Adam Mickiewicz": {
        'subject': ["chemia"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Popiełuszko": {
        'subject': ["religia"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': None,
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': None
        }
    },
    "Wiz Khalifa": {
        'subject': ["biologia"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    },
    "Moj Stary": {
        'subject': ["fizyka"],
        'work_hours': {
            'Monday': [1, 2, 3, 4, 5],
            'Tuesday': [1, 2, 3, 4, 5],
            'Wednesday': [1, 2, 3, 4, 5],
            'Thursday': [1, 2, 3, 4, 5],
            'Friday': [1, 2, 3, 4, 5]
        }
    }
}
GROUP = {
    'IB': {
        "matematyka": [8, None],
        "fizyka": [4, None],
        "j.polski": [6, None],
        "biologia": [2, None],
        "chemia": [1, None],
        "wf": [2, None],
        "religia": [2, None],
    },
    'IA': {
        "matematyka": [6, None],
        "fizyka": [2, None],
        "j.polski": [4, None],
        "biologia": [4, None],
        "chemia": [3, None],
        "wf": [4, None],
        "religia": [2, None]
    },
    'IC': {
        "matematyka": [5, None],
        "fizyka": [4, None],
        "j.polski": [4, None],
        "biologia": [2, None],
        "chemia": [4, None],
        "wf": [4, None],
        "religia": [2, None]
    },
    'ID': {
        "matematyka": [6, None],
        "fizyka": [2, None],
        "j.polski": [7, None],
        "biologia": [3, None],
        "chemia": [2, None],
        "wf": [4, None],
        "religia": [1, None]
    },
    'IIA': {
        "matematyka": [4, "Janusz Walczuk"],
        "fizyka": [2, "Albert Einstein"],
        "j.polski": [7, "Krystyna Pawłowicz"],
        "biologia": [3, "Snoop Dogg"],
        "chemia": [2, "Waldemar Kiepski"],
        "wf": [4, "Robert Lewandowski"],
        "religia": [1, None]
    }

}

ToughSubjects = ("matematyka", "fizyka", "j.polski", "biologia", "chemia")


class Classroom:
    """
        Class Classroom is representation of data about classrooms in school
    """

    def __init__(self, class_number, preferred_subject):
        self.class_number = class_number
        self.preferred_subject = preferred_subject


class Teacher:
    """
        Class Techer is representation of data about teachers in school
    """

    def __init__(self, name: string, data: dict):
        self.name = name
        self.data = data
        self.subject = self.__set_subject()
        self.preferred_work_hours = self.__set_preferred_work_hours()
        self.work_hours = 0

    def __set_subject(self):
        return self.data['subject']

    def __set_preferred_work_hours(self):
        return self.data['work_hours']

    def increase_work_hours(self, hours):
        self.work_hours += hours


class Group:
    """
        Classroom is representation of data about groups of students in school
    """

    def __init__(self, group_name: string, subjects: dict, tough_subjects=ToughSubjects):
        self.name = group_name
        self.subjects = subjects
        self.list_of_subjects = []
        self.list_of_tough_subjects = tough_subjects
        self.lessons_per_week = self.__set_lessons_per_week()
        self.max_lessons_per_day = self.__set_max_lessons_per_day()
        self.min_lessons_per_day = self.__set_min_lessons_per_day()
        self.max_tough_lessons_per_day = self.__set_max_tough_lessons_per_day()
        self.preferred_teachers = self.__set_preferred_teachers()
        self.__set_list_of_subjects()

    def set_list_of_subjects_call(self):
        self.__set_list_of_subjects()

    def __set_list_of_subjects(self):
        temp = []
        for key, value in self.subjects.items():
            # value[0] is number of subject per week
            for _ in range(value[0]):
                temp.append([key, value[1]])
        for _ in range(10):
            shuffle(temp)
        self.list_of_subjects = temp

    def __set_lessons_per_week(self):
        count = 0
        for value in self.subjects.values():
            count += value[0]
        return count

    def __set_max_lessons_per_day(self):
        return self.lessons_per_week / 5 + 1

    def __set_min_lessons_per_day(self):
        return self.lessons_per_week / 5 - 1

    def __set_max_tough_lessons_per_day(self):
        count = 0
        for key, value in self.subjects.items():
            if key in self.list_of_tough_subjects:
                count += value[0]
        return count / 5

    def __set_preferred_teachers(self):
        temp = {}
        for subject, teacher in self.subjects.items():
            if teacher[1] is not None:
                temp[teacher[1]] = {'subject': subject, 'hours': teacher[0]}
        if len(temp) == 0:
            temp = None
        return temp

    def get_preferred_teacher_work_hours(self, teacher_name: str):
        return self.preferred_teachers[teacher_name]['hours']

    def set_teacher_of_subject(self, subject_name, teacher_name):
        subject_to_set = self.subjects[subject_name]
        subject_to_set[1] = teacher_name
        self.subjects[subject_name] = subject_to_set
        self.__set_list_of_subjects()


class School:
    """
        Class School is representation of data about all of instances in school
    """
    def __init__(self, groups_data: dict, teachers_data: dict, classrooms_data: dict, classroom_req: set):
        self.school_name = None
        self.classrooms = self.__process_classrooms(classrooms_data)
        self.classrooms_set = self.__process_classrooms_to_set()
        self.classrooms_data = classrooms_data
        self.classroom_req = classroom_req
        self.groups = self.__process_groups(groups_data)
        self.list_of_tough_subjects = self.groups.copy().popitem()[1].list_of_tough_subjects
        self.teachers = self.__process_teachers(teachers_data)
        self.max_lessons_per_day_for_school = self.__set_max_lessons_per_day()
        self.__assign_teachers_to_groups()
        self.list_of_all_subjects = self.__process_list_of_all_subjects()

    def get_req_name(self, sub_name):
        if sub_name not in self.classroom_req:
            return 'zw'
        return sub_name

    def __assign_teachers_to_groups(self):
        """
            Assigns teachers to all of groups with unassigned teachers
        """
        list_of_subjects_without_teacher = []
        # Make list of all subjects from groups without teaher assigned
        for group in self.groups.values():
            for subject_name, data in group.subjects.items():
                teacher_name = data[1]
                subject_hours = data[0]
                if teacher_name is None:
                    list_of_subjects_without_teacher.append([group.name, subject_name, subject_hours])

        # Assign teacher to subject of class
        for subject in list_of_subjects_without_teacher:
            # Just for easier coding
            group_name = subject[0]
            subject_name = subject[1]
            subject_hours = subject[2]
            teachers_of_this_subject = []

            # Make list of teachers teaching the subject which we are looking for
            for teacher in self.teachers.values():
                if subject_name in teacher.subject:
                    teachers_of_this_subject.append(teacher)

            # Look for teacher witch the smallest amount of hours
            teacher_not_busy = teachers_of_this_subject[0]
            for teacher in teachers_of_this_subject:
                if teacher.work_hours < teacher_not_busy.work_hours:
                    teacher_not_busy = teacher

            # Assign teacher to class
            self.groups[group_name].set_teacher_of_subject(teacher_name=teacher_not_busy.name,
                                                           subject_name=subject_name)
            # Increase teacher's work hours
            self.teachers[teacher_not_busy.name].increase_work_hours(subject_hours)

    def __set_max_lessons_per_day(self):
        max_lessons = 0
        for group_name, group in self.groups.items():
            if group.max_lessons_per_day > max_lessons:
                max_lessons = group.max_lessons_per_day
        return max_lessons

    @staticmethod
    def __process_groups(school_class_data):
        temp = {}
        for group, subjects in school_class_data.items():
            temp[group] = Group(group_name=group, subjects=subjects)
        return temp

    def __process_teachers(self, teachers_data):
        temp = {}
        for name, data in teachers_data.items():
            temp[name] = Teacher(name=name, data=data)
        groups_with_teachers = [group for group in self.groups.values() if group.preferred_teachers is not None]
        for group in groups_with_teachers:
            for teacher in temp.values():
                if teacher.name in group.preferred_teachers:
                    teacher.work_hours += group.get_preferred_teacher_work_hours(teacher_name=teacher.name)
        return temp

    @staticmethod
    def __process_classrooms(classes_data):
        temp = []
        for class_number, preferred_subject in classes_data.items():
            temp.append(Classroom(class_number=class_number, preferred_subject=preferred_subject))
        return temp

    def __process_classrooms_to_set(self):
        temp = set()
        for classroom_number in self.classrooms:
            temp.add(classroom_number)
        return temp

    def __process_list_of_all_subjects(self):
        temp = []
        for group_name, group in self.groups.items():
            for sub in group.list_of_subjects:
                temp.append([group.name, *sub, None])
        for _ in range(10):
            shuffle(temp)
        return temp
