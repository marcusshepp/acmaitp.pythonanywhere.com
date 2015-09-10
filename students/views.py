from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Student
from .forms import StudentForm


class CreateStudent(View):

    template_name = "students/create_student.html"

    def get(self, request, *a, **kw):
        context = {}
        context["form"] = StudentForm()
        return render(request, self.template_name, context)

    def post(self, request, *a, **kw):
        obj = dict(request.POST.items())
        obj.pop(u"csrfmiddlewaretoken")
        if obj["programming_experience"] == u"":
            obj["programming_experience"] = 0
        Student.objects.get_or_create(**obj)
        return redirect("/")


class StudentEmails(View):
    
    template_name = "students/student_emails.html"

    def get(self, request, *a, **kw):
        context = {}
        students = Student.objects.all()
        num_of_students = Student.objects.all().count()
        context["students"] = students
        context["num_of_students"] = num_of_students
        return render(request, self.template_name, context)
