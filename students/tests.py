from django.test import TestCase

from .models import (
    Student,
    Officer,
    Position
)


class SimpleTest(TestCase):

    string = "string"
    num = 1
    boolean = False

    def test_create_objects(self):
        student = {
            "first_name": self.string,
            "last_name": self.string,
            "email": "string@string.com",
            "academic_standing": "sophomore",
            "major": self.string,
            "programming_experience": self.num,
            "laptop_bool": self.boolean,
            "laptop_info": self.string,
            "method_of_discovery": "poster",
            "officer_bool": self.boolean,
        }
        students = Student.objects.get_or_create(**student)
        student_has_been_created = Student.objects.filter(
            **student).exists()
        self.assertTrue(student_has_been_created)
        position = {
            "title": self.string,
            "responsibilities": self.string,
        }
        positions = Position.objects.get_or_create(**position)
        position_has_been_created = Position.objects.filter(
            **position).exists()
        self.assertTrue(position_has_been_created)
        get_position = Position.objects.get(id=1)
        student["position"] = get_position
        student["years_involved"] = self.num
        officers = Officer.objects.get_or_create(**student)
        officer_has_been_created = Officer.objects.filter(
            **student).exists()
        self.assertTrue(officer_has_been_created)
