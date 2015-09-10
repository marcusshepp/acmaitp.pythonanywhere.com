from django.contrib import admin

from .models import (
    Student,
    Officer,
    Position
)

admin.site.register(Student)
admin.site.register(Officer)
admin.site.register(Position)
