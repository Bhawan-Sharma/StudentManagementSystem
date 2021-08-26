from django.db import models

# Create your models here.

class Company(models.Model):
    cName = models.CharField(primary_key='true',max_length=50,unique='true')
    cEmail = models.EmailField()
    cLogo = models.ImageField(upload_to="images", blank=True)
    cUrl = models.CharField(max_length=50)
    class Meta:
        db_table = "company"

class Employee(models.Model):
    eFname = models.CharField(primary_key='true',max_length=50,unique='true')
    eLname = models.CharField(max_length=50)
    eCompany = models.ForeignKey(Company, on_delete=models.CASCADE)
    eEmail = models.EmailField()
    ePhone = models.CharField(max_length=50)
    class Meta:
        db_table = "employee"

class StudentDetails(models.Model):
    sRollno=models.IntegerField()
    sName=models.CharField(primary_key='true',max_length=50,unique='true')
    sAddress=models.CharField(max_length=50)
    sEmail=models.EmailField()
    sCourse=models.CharField(max_length=20)
    sFeeStatus=models.CharField(max_length=15)

    class Meta:
        db_table="StudentDetails"


class StudentResult(models.Model):
    STATUS = (
        ('Passed', 'Passed'),
        ('Failed', 'Failed'),
    )
    Rollno=models.IntegerField()
    Name=models.CharField(primary_key='true',max_length=50,unique='true')
    Course=models.CharField(max_length=20)
    MaxMarks=models.IntegerField()
    MarksObtained=models.IntegerField()
    Result=models.CharField(max_length=50, null=True, choices=STATUS)
    class Meta:
        db_table="StudentResult"