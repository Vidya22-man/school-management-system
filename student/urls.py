from django.urls import path
from student import views

urlpatterns=[
    path('',views.all_students,name='all_students'),
    path('add_student/',views.add_student,name="add_student"),
    path('edit/<uuid:pk>',views.edit_student,name="edit_student"),
    path('delete_student/<uuid:pk>',views.delete_student,name="delete_student"),




]