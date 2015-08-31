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
        labels = {
            "email": "CMich Email",
            "programming_experience": "Programming Experience from 1-10",
            "laptop": "Do you have a laptop",
            "laptop_info": "If so, what is the model and Operating System?",
            "method_of_discovery": "How did you hear about ACM/AITP?",
        }
        widgets = {
			"email": forms.EmailInput(),
		}