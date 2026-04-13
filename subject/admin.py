from django.contrib import admin
from . models import Standard,Subject,Teacher

# Register your models here.
admin.site.register(Standard)

class TeacherAdmin(admin.ModelAdmin):
    list_display = ('staff',)
    list_display_links = ('staff',)

admin.site.register(Teacher,TeacherAdmin)

class SubjectAdmin(admin.ModelAdmin):
    list_display = ('subject_name','code','standard','teacher')
    list_display_links = ('subject_name', 'code', 'standard', 'teacher')

admin.site.register(Subject,SubjectAdmin)
