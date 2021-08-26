from django.contrib import admin
from .models import StudentDetails,StudentResult,Company,Employee
# Register your models here.

admin.site.register(StudentDetails)
admin.site.register(StudentResult)
admin.site.register(Company)
admin.site.register(Employee)
