from django.forms import ModelForm, ValidationError
from django import forms

from . import models


class GradeForm(ModelForm):
    class Meta:
        model = models.Grade
        fields = ['name', 'workingDay', 'available']


class EmployeeForm(ModelForm):
    class Meta:
        model = models.Employee
        fields = [
            'name',
            'lastName',
            'document',
            'email',
            'age',
            'role',
            'workingDay',
            'available'
        ]


# VALIDATIONS FOR CREATE ASSIGNMENT
class AssignGradeForm(ModelForm):
    class Meta:
        model = models.Holder
        fields = ['employee', 'grade']

    def clean(self):
        cleaned_data = super().clean()
        employee = cleaned_data['employee']
        grade = cleaned_data['grade']

        if employee.workingDay != grade.workingDay:
            message = 'It must be the same Working Day for the employee and the grade'
            code = 'Invalid'
            raise ValidationError(message, code=code)

        list_ = models.Holder.objects.filter(employee=employee, grade=grade, available=True)

        if len(list_) > 0:
            message = 'Already exist'
            code = 'Invalid'
            raise ValidationError(message, code=code)


# PROBLEMS WITH VALIDATIONS TO UPDATE (SOLUTION: THIS FORM)
class AssignGradeUpdate(AssignGradeForm):
    def clean(self):
        return ModelForm.clean(self)
