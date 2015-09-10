from django.conf.urls import include, url

from .views import CreateStudent, StudentEmails

urlpatterns = [
    url(r'^signup/$', CreateStudent.as_view(), name="signup"),
    url(r'^emails/$', StudentEmails.as_view(), name="emails"),
]
