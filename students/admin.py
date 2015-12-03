from django.contrib import admin

from .models import (
    Student,
    Officer,
    Position,
    TechTalk
)

admin.site.register(Student)
admin.site.register(Officer)
admin.site.register(Position)
admin.site.register(TechTalk)
