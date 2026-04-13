from django import forms
from .models import Subject,Standard,Staff,Teacher


class StandardForm(forms.ModelForm):
    class Meta:
        model=Standard
        fields=('name',)

class TeacherForm(forms.ModelForm):
    class Meta:
        model=Teacher
        fields=('staff',)

class SubjectForm(forms.ModelForm):
    class Meta:
        model=Subject
        fields=('subject_name','code','standard','teacher')

