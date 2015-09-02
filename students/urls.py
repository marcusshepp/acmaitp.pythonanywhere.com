from django.conf.urls import include, url

from .views import CreateStudent

urlpatterns = [
    url(r'^$', CreateStudent.as_view(), name="signup"),
]
