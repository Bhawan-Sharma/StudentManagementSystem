from django import forms
from .models import Employee,Company,StudentResult,StudentDetails


# This is for employee
class EmployeeForm(forms.ModelForm):
    class Meta:
        model = Employee
        fields = "__all__"

#this is for company
class CompanyForm(forms.ModelForm):
    class Meta:
        model = Company
        fields = "__all__"

class StudentResultForm(forms.ModelForm):
    class Meta:
        model = StudentResult
        fields = "__all__"

#this is for company
class StudentDetailsForm(forms.ModelForm):
    class Meta:
        model = StudentDetails
        fields = "__all__"
