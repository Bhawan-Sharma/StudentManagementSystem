from django.shortcuts import render,redirect

from .forms import CompanyForm,EmployeeForm,StudentResultForm,StudentDetailsForm
from .models import Employee,Company,StudentResult,StudentDetails
from .utils import get_plot

from django.contrib import messages
from django.contrib.auth.models import User,auth



#Home page
def home(request):
    return redirect(request,"")


# To create Company
def comp(request):
    if request.method == "POST":

        form = StudentDetailsForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/show")
            except:
                pass
    else:
        form = StudentDetailsForm()
    return render(request, "index.html", {'form':form})

# To retrieve Company details
def show(request):
    students = StudentDetails.objects.all()
    return render(request, "show.html", {'students':students})

# To Edit Company details
def edit(request, sName):
    student = StudentDetails.objects.get(sName=sName)
    return render(request, "edit.html", {'student':student})

# To Update Company
def update(request, sName):
    student = StudentDetails.objects.get(sName=sName)
    form = StudentDetailsForm(request.POST, instance= student)
    if form.is_valid():
        form.save()
        return redirect("/show")
    return render(request, "edit.html", {'student': student})

# To Delete Company details
def delete(request, sName):
    student = StudentDetails.objects.get(sName=sName)
    student.delete()
    return redirect("/show")


# To create employee
def emp(request):
    if request.method == "POST":
        form = StudentResultForm(request.POST)
        if form.is_valid():
            try:
                form.save()
                return redirect("/showemp")
            except:
                pass
    else:
        form = StudentResultForm()
    return render(request, "addemp.html", {'form':form})

# To show employee details
def showemp(request):
    employees = StudentResult.objects.all()
    return render(request, "showemp.html", {'employees':employees})

# To delete employee details
def deleteEmp(request, Name):
    employee = StudentResult.objects.get(Name=Name)
    employee.delete()
    return redirect("/showemp")

# To edit employee details
def editemp(request, Name):
    employee = StudentResult.objects.get(Name=Name)
    return render(request, "editemployee.html", {'employee':employee})

# To update employee details
def updateEmp(request, Name):
    employee = StudentResult.objects.get(Name=Name)
    form = StudentResultForm(request.POST, instance= employee)
    print('Hello1')
    if form.is_valid():
        form.save()
        return redirect("/showemp")
    return render(request, "editemployee.html", {'employee': employee})


def main_view(request):
    qs = StudentResult.objects.all()
    x = [x.Name for x in qs]
    y = [y.MarksObtained for y in qs]
    z= [z.Rollno for z in qs]
    chart = get_plot(x,y,z)


    return render(request,'main.html',{'chart': chart})