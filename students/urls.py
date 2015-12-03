from django.conf.urls import include, url

from .views import CreateStudent, StudentEmails, CreateTeckTalk

urlpatterns = [
    url(r'^signup/$', CreateStudent.as_view(), name="signup"),
    url(r'^techtalk/$', CreateTeckTalk.as_view(), name="techtalk"),
    url(r'^emails/$', StudentEmails.as_view(), name="emails"),
]
