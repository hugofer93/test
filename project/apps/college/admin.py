from django.contrib import admin

from . import models


# Register your models here.
@admin.register(models.Role)
class Role(admin.ModelAdmin):
    list_display = ['name']
    list_display_links = ['name']
    search_fields = ['name']
    list_filter = ['name']


@admin.register(models.WorkingDay)
class WorkingDay(admin.ModelAdmin):
    list_display = ['schedule']
    list_display_links = ['schedule']
    search_fields = ['schedule']
    list_filter = ['schedule']


@admin.register(models.Employee)
class Employee(admin.ModelAdmin):
    list_display = ['name', 'lastName', 'document', 'email', 'registrationDate']
    list_display_links = ['name']
    search_fields = ['name', 'lastName', 'document', 'email']
    list_filter = ['role']


@admin.register(models.Grade)
class Grade(admin.ModelAdmin):
    list_display = ['name', 'workingDay']
    list_display_links = ['name']
    search_fields = ['name', 'workingDay__schedule']
    list_filter = ['name']


@admin.register(models.Holder)
class Holder(admin.ModelAdmin):
    list_display = ['employee', 'grade']
    list_display_links = ['employee']
    search_fields = [
        'employee__name',
        'employee__lastName',
        'employee__workingDay',
        'employee__document',
        'employee__email',
        'grade__name',
        'grade__workingDay'
    ]
    list_filter = [
        'employee',
        'employee__workingDay',
        'grade',
        'grade__workingDay'
    ]
