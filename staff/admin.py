from django.contrib import admin
from .models import Staff,StaffAttendance

# Register your models here.

class StaffAdmin(admin.ModelAdmin):
    list_display = ('employee_id','full_name','role','gender','birth_date','address','email','mobile_no','qualification','salary')
    list_display_links = ('employee_id','full_name','role','gender','birth_date','address','email')
admin.site.register(Staff,StaffAdmin)



class StaffAttendanceAdmin(admin.ModelAdmin):
    list_display = ('staff','date','status')
    list_display_links= ('staff', 'date', 'status')

admin.site.register(StaffAttendance,StaffAttendanceAdmin)