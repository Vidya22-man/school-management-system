from django.contrib import admin
from student.models import Student,Father

# Register your models here.


class FatherAdmin(admin.ModelAdmin):
    list_display =['father_name','mother_name','birth_date','address','occupation','mobile_no','caste']
    list_display_links = ['father_name','mother_name']

admin.site.register(Father,FatherAdmin)


class StudentAdmin(admin.ModelAdmin):
    list_display=['first_name','last_name','father','birth_date','caste','gender','religion','photo']
    list_display_links = ['first_name','last_name','father','birth_date','caste','gender','religion','photo']


admin.site.register(Student,StudentAdmin)
