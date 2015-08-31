# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('first_name', models.CharField(max_length=50)),
                ('last_name', models.CharField(max_length=50)),
                ('email', models.CharField(max_length=50)),
                ('academic_standing', models.CharField(max_length=50, choices=[(b'freshman', b'Freshman'), (b'sophomore', b'Sophomore'), (b'junior', b'Junior'), (b'senior', b'Senior'), (b'grad', b'Graduate')])),
                ('major', models.CharField(max_length=100)),
                ('programming_experience', models.PositiveSmallIntegerField()),
                ('laptop_bool', models.BooleanField(default=False)),
                ('laptop_info', models.CharField(max_length=100)),
                ('method_of_discovery', models.CharField(max_length=50, choices=[(b'poster', b'A Poster'), (b'friend', b'A friend refered me'), (b'email', b'Got an email'), (b'class', b'Someone came to my class'), (b'professor', b'A professor refered me'), (b'stumbled', b'Just happened to stumble upon')])),
            ],
        ),
    ]
