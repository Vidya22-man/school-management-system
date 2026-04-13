from django import forms
from .models import Staff,StaffAttendance


class StaffForm(forms.ModelForm):
    class Meta:
        model=Staff
        fields = '__all__'

class StaffAttendanceForm(forms.ModelForm):
    class Meta:
        model=StaffAttendance
        fields='__all__'


