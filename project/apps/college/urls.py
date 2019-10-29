from django.urls import path

from . import views

app_name = 'college'

urlpatterns = [
    path('', views.Index.as_view(), name='index'),
    path('grade/', views.GradeList.as_view(), name='gradeList'),
    path('grade/add/', views.AddGrade.as_view(), name='addGrade'),
    path('grade/<int:id>/', views.GradeDetail.as_view(), name='gradeDetail'),

    path('employee/', views.EmployeeList.as_view(), name='employeeList'),
    path('employee/add/', views.AddEmployee.as_view(), name='addEmployee'),
    path('employee/<int:id>/', views.EmployeeDetail.as_view(), name='employeeDetail'),

    path('assignment/', views.AssignmentList.as_view(), name='assignmentList'),
    path('assign/grade/', views.AssignGrade.as_view(), name='assignGrade'),
    path('assignment/<int:id>/', views.AssignmentDetail.as_view(), name='assignmentDetail'),
    path('assignment/<int:id>/delete', views.AssignmentDelete.as_view(), name='assignmentDelete')
]
