from django.urls import path
from subject import views

urlpatterns=[
    path('',views.subject_list,name='subject_list'),
    path('add_subject/',views.add_subject,name="add_subject"),
    path('edit_subject/<int:pk>',views.edit_subject,name="edit_subject"),
    path('delete_subject/<int:pk>',views.delete_subject,name="delete_subject"),



]