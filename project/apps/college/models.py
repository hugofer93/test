#from django.contrib.auth.models import User
from django.db import models
from django.urls import reverse


# Create your models here.
class Role(models.Model):
    TEACHER = 'teacher'
    ROLE_CHOICES = (
        (TEACHER, 'teacher'),
    )

    name = models.CharField(
        max_length=15,
        unique=True,
        choices=ROLE_CHOICES
    )

    def __str__(self):
        return self.name


class WorkingDay(models.Model):
    MORNING = 'morning'
    AFTERNOON = 'afternoon'
    WORKINGDAY_CHOICES = (
        (MORNING, 'morning'),
        (AFTERNOON, 'afternoon'),
    )

    schedule = models.CharField(
        max_length=15,
        unique=True,
        choices=WORKINGDAY_CHOICES
    )

    def __str__(self):
        return self.schedule


class Grade(models.Model):
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=45)
    workingDay = models.ForeignKey(WorkingDay, on_delete=models.CASCADE)

    available.Boolean = True

    def __str__(self):
        return '{} - {}'.format(self.name, self.workingDay)

    def get_absolute_url(self):
        return reverse('college:gradeDetail', kwargs={'id': self.id})


class Employee(models.Model):
    # eliminated for time reasons 
    # user = models.OneToOneField(User,on_delete=models.CASCADE)
    available = models.BooleanField(default=True)
    name = models.CharField(max_length=45)
    lastName = models.CharField(max_length=45)
    document = models.CharField(max_length=10, unique=True)
    email = models.EmailField(unique=True)
    age = models.IntegerField()
    registrationDate = models.DateField(auto_now_add=True)
    role = models.ForeignKey(Role, on_delete=models.CASCADE)
    workingDay = models.ForeignKey(WorkingDay, on_delete=models.CASCADE)
    grade = models.ManyToManyField(Grade, through='Holder')

    available.Boolean = True

    def __str__(self):
        return self.getFullName()

    def getFullName(self):
        return '{} {}'.format(self.name, self.lastName)

    def get_absolute_url(self):
        return reverse('college:employeeDetail', kwargs={'id': self.id})


class Holder(models.Model):
    available = models.BooleanField(default=True)
    employee = models.ForeignKey(Employee, on_delete=models.CASCADE)
    grade = models.ForeignKey(Grade, on_delete=models.CASCADE)

    available.Boolean = True

    def __str__(self):
        return '{} - {}'.format(self.employee, self.grade)

    def get_absolute_url(self):
        return reverse('college:assignmentDetail', kwargs={'id': self.id})
