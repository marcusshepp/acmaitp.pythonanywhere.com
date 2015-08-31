from django.conf.urls import include, url

from .views import CreateStudent

urlpatterns = [
    url(r'signup/^', CreateStudent.as_view()),
]
