from django.db import models
from staff.models import Staff


# Create your models here.
class Standard(models.Model):
    name=models.CharField(max_length=150)

    def __str__(self):
        return self.name

class Teacher(models.Model):
    staff=models.OneToOneField(Staff,on_delete=models.CASCADE,limit_choices_to={'role':'Teaching'})

    def  __str__(self):
        return self.staff.full_name


class Subject(models.Model):
    subject_name=models.CharField(max_length=150,help_text="Enter Subject Name")
    code=models.CharField(max_length=100,help_text="Enter Subject Code. E.g.. Mara05,HIND05")
    standard=models.ForeignKey(Standard,on_delete=models.CASCADE)
    teacher=models.ForeignKey(Teacher,on_delete=models.SET_NULL,null=True,blank=True,related_name="subjects")

    def __str__(self):
        return self.subject_name