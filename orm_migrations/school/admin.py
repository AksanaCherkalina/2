from django.contrib import admin
from .models import Student, Teacher, StudentPosition
# from jmespath import search

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
    # list_display = ['name', 'teacher', 'group']
    # list_display = ['group']
    pass


@admin.register(Teacher)
class TeacherAdmin(admin.ModelAdmin):
    list_display = ['name', 'subject']
    list_display = ['subject']
    # pass
