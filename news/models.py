from django.db import models

from acm.settings import MEDIA_URL


class Update(models.Model):

    class Meta:
        ordering = ['-pk']

    datetime = models.DateTimeField(auto_now_add=True)
    when = models.DateTimeField()
    where = models.CharField(max_length=100)
    what = models.CharField(max_length=100)
    
    def __unicode__(self):
        return "{0} - {1}".format(self.what, self.where)


class Link(models.Model):

    class Meta:
        ordering = ['-pk']

    title = models.CharField(max_length=200)
    problem = models.FileField(upload_to=MEDIA_URL, blank=True, null=True)
    link = models.CharField(max_length=200, blank=True, null=True)
    
    def __unicode__(self):
        return "{0}".format(self.title)
