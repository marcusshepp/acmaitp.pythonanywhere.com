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
        Student.objects.get_or_create(**obj)
        return redirect("/")
