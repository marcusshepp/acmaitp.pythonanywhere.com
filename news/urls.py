from django.conf.urls import include, url

from .views import UpdateFeed

urlpatterns = [
    url(r'^$', UpdateFeed.as_view()),
]
