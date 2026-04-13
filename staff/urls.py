from django.urls import path

from staff import views

urlpatterns = [
    path('', views.staff_list, name='all_staff_list'),
    path('add_staff/', views.add_staff, name="add_staff"),
    path('edit_staff/<uuid:pk>/', views.edit_staff, name="edit_staff"),
    path('delete_staff/<uuid:pk>/', views.delete_staff, name="delete_staff"),

    # -------------------------------end staff section---->

    path('staff_attendance/', views.staff_attendance, name="staff_attendance"),
    path('add_staff_attendance/', views.add_staff_attendance, name="add_staff_attendance"),
    path('edit_staff_attendance/<int:pk>',views.edit_staff_attendance,name="edit_staff_attendance"),
    path('delete_staff_attendance<int:pk>',views.delete_staff_attendance,name="delete_staff_attendance"),




]
