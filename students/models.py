from django.db import models


class Student(models.Model):

    ACADEMIC_STANDING_CHOICES = [
        ("freshman", "Freshman"),
        ("sophomore", "Sophomore"),
        ("junior", "Junior"),
        ("senior", "Senior"),
        ("grad", "Graduate")
    ]
    METHOD_OF_DISCOVERY_CHOICES = [
        ("poster", "A Poster"),
        ("friend", "A friend refered me"),
        ("email", "Got an email"),
        ("class", "Someone came to my class"),
        ("professor", "A professor refered me"),
        ("stumbled", "Just happened to stumble upon")
    ]
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    email = models.CharField(max_length=50)
    academic_standing = models.CharField(
        max_length=50, choices=ACADEMIC_STANDING_CHOICES)
    major = models.CharField(max_length=100)
    programming_experience = models.PositiveSmallIntegerField()
    laptop_bool = models.BooleanField(default=False)
    laptop_info = models.CharField(max_length=100)
    method_of_discovery = models.CharField(
        max_length=50, choices=METHOD_OF_DISCOVERY_CHOICES)
    officer_bool = models.NullBooleanField(blank=True, null=True)

    def __unicode__(self):
        return self.first_name


class Officer(Student):

    position = models.ForeignKey("Position");
    years_involved = models.PositiveSmallIntegerField(
        blank=True, null=True)


class Position(models.Model):

    title = models.CharField(max_length=50, blank=True, null=True)
    responsibilities = models.CharField(
        blank=True, null=True, max_length=50)

    def __unicode__(self):
        return "{0}".format(self.title)
