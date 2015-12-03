# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0002_auto_20150910_0055'),
    ]

    operations = [
        migrations.CreateModel(
            name='TechTalk',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('full_name', models.CharField(max_length=100)),
                ('title_of_talk', models.CharField(max_length=100)),
                ('when', models.DateTimeField()),
                ('email', models.CharField(max_length=50)),
            ],
        ),
    ]
