from django.db import models


class Update(models.Model):

    datetime = models.DateTimeField(auto_now_add=True)
    when = models.DateTimeField()
    where = models.CharField(max_length=100)
    what = models.CharField(max_length=100)
