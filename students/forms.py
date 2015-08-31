from django import forms

from .models import Student


class StudentForm(forms.ModelForm):
    
    class Meta:
        model = Student
        fields = [
            "first_name",
            "last_name",
            "email",
            "academic_standing",
            "major",
            "programming_experience",
            "laptop_bool",
            "laptop_info",
            "method_of_discovery",
        ]