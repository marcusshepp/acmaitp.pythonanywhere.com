# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
        ('students', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Officer',
            fields=[
                ('student_ptr', models.OneToOneField(parent_link=True, auto_created=True, primary_key=True, serialize=False, to='students.Student')),
                ('years_involved', models.PositiveSmallIntegerField(null=True, blank=True)),
            ],
            bases=('students.student',),
        ),
        migrations.CreateModel(
            name='Position',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('title', models.CharField(max_length=50, null=True, blank=True)),
                ('responsibilities', models.CharField(max_length=50, null=True, blank=True)),
            ],
        ),
        migrations.AddField(
            model_name='student',
            name='officer_bool',
            field=models.NullBooleanField(),
        ),
        migrations.AddField(
            model_name='officer',
            name='position',
            field=models.ForeignKey(to='students.Position'),
        ),
    ]
