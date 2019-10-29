from django.urls import reverse_lazy
from django.http.response import HttpResponseRedirect
from django.views.generic import (
    TemplateView,
    CreateView,
    ListView,
    UpdateView,
    DeleteView
)

from . import forms
from . import models


# Create your views here.
class Index(TemplateView):
    http_method_names = ['get']
    template_name = 'college/index.html'


class GradeList(ListView):
    http_method_names = ['get']
    model = models.Grade
    queryset = model.objects.filter(available=True)
    template_name = 'college/gradeList.html'


class AddGrade(CreateView):
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('college:gradeList')
    form_class = forms.GradeForm
    template_name = 'college/addGrade.html'


class GradeDetail(UpdateView):
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('college:gradeList')
    model = models.Grade
    form_class = forms.GradeForm
    pk_url_kwarg = 'id'
    template_name = 'college/gradeDetail.html'


class EmployeeList(ListView):
    http_method_names = ['get']
    model = models.Employee
    queryset = model.objects.filter(available=True)
    template_name = 'college/employeeList.html'


class AddEmployee(CreateView):
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('college:employeeList')
    form_class = forms.EmployeeForm
    template_name = 'college/addEmployee.html'


class EmployeeDetail(UpdateView):
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('college:employeeList')
    model = models.Employee
    form_class = forms.EmployeeForm
    pk_url_kwarg = 'id'
    template_name = 'college/employeeDetail.html'


class AssignmentList(ListView):
    http_method_names = ['get']
    model = models.Holder
    queryset = model.objects.filter(available=True).order_by('-employee')
    template_name = 'college/assignmentList.html'


class AssignGrade(CreateView):
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('college:assignmentList')
    form_class = forms.AssignGradeForm
    template_name = 'college/assignGrade.html'


class AssignmentDetail(UpdateView):
    http_method_names = ['get', 'post']
    success_url = reverse_lazy('college:assignmentList')
    model = models.Holder
    form_class = forms.AssignGradeUpdate
    pk_url_kwarg = 'id'
    template_name = 'college/assignmentDetail.html'


class AssignmentDelete(DeleteView):
    http_method_names = ['get', 'post']
    model = models.Holder
    pk_url_kwarg = 'id'
    template_name = 'college/assignmentDeleteConfirm.html'

    def delete(self, request, *args, **kwargs):
        """
        Call the delete() method on the fetched object and then redirect to the
        success URL.
        """
        self.object = self.get_object()
        success_url = reverse_lazy('college:assignmentList')
        self.object.available = False
        self.object.save()
        return HttpResponseRedirect(success_url)
