from django import forms
from student.models import Student,Father

class StudentForm(forms.ModelForm):
    class Meta:
        model=Student
        fields=('first_name','last_name','father','birth_date','caste','gender','religion','standard','enrollment_status','photo')

class FatherForm(forms.ModelForm):
    class Meta:
        model=Father
        fields=('father_name','mother_name','birth_date','address','occupation','mobile_no','caste')
