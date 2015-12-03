import csv, datetime

from django.http import HttpResponse
from django.shortcuts import render, redirect
from django.views.generic import View

from .models import Student, TechTalk
from .forms import StudentForm, TechTalkForm


class CreateStudent(View):

    template_name = "students/form.html"

    def get(self, request, *a, **kw):
        context = {}
        context["form"] = StudentForm()
        context["form_name"] = "Email Updates"
        return render(request, self.template_name, context)

    def post(self, request, *a, **kw):
        obj = dict(request.POST.items())
        obj.pop(u"csrfmiddlewaretoken")
        if obj["programming_experience"] == u"":
            obj["programming_experience"] = 0
        Student.objects.get_or_create(**obj)
        return redirect("/")


class CreateTeckTalk(View):

    template_name = "students/form.html"

    def get(self, request, *a, **kw):
        context = {}
        context["form"] = TechTalkForm()
        context["form_name"] = "2016 TechTalk"
        return render(request, self.template_name, context)

    def post(self, request, *a, **kw):
        day = request.POST["when_day"]
        if len(day) < 2:
            day = "0" + day
        month = request.POST["when_month"]
        if len(month) < 2:
            month =  "0" + month
        year = request.POST["when_year"]
        date = month + "/" + day + "/" + year
        date = datetime.datetime.strptime(str(date), "%m/%d/%Y")
        data = {
            "full_name": str(request.POST["full_name"]),
            "title_of_talk": str(request.POST["title_of_talk"]),
            "when": date.date(),
            "email": str(request.POST["email"]),
        }
        TechTalk.objects.create(**data)
        return render(request, "students/thanks.html")


class StudentEmails(View):

    template_name = "students/student_emails.html"

    def email_to_csv(self, data, file_name, *args, **kwargs):
        """
        This function is designed to dump a views table data into a CSV file.
        Notice that you can not pick which catagories/columns you want to exclude
        from the CSV. *data* must be a list of dictionaries that contains only
        the fields that the permission group is allowed to see.
        """
        response = HttpResponse(content_type='text/csv')
        response['Content-Disposition'] = 'attachment; filename="{}.csv"'.format(file_name)
        # writing the csv data to a response object.
        w = csv.writer(response)
        w.writerow(data)
        return response

    def student_data(self):
        context = {}
        students = Student.objects.all()
        num_of_students = students.count()
        for student in students:
            if student.first_name == "":
                context["students"] = students.exclude(pk=student.pk)
            else:
                context["students"] = students
        context["num_of_students"] = num_of_students
        return context

    def post(self, request, *a, **kw):
        student_data = self.student_data()
        student_email = [x.email for x in student_data["students"]]
        return self.email_to_csv(student_email, file_name="acm_aitp_student_emails")

    def get(self, request, *a, **kw):
        context = self.student_data()
        return render(request, self.template_name, context)
