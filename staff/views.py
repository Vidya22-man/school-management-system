from django.shortcuts import render,redirect,get_object_or_404,HttpResponse
from .models import Staff,StaffAttendance
from .forms import StaffForm,StaffAttendanceForm
from django.contrib import messages
from django.db.models import Q
from django.utils import timezone
import openpyxl
from calendar import monthrange
from datetime import datetime

# Create your views here.
def staff_list(request):
    query=request.GET.get('q')
    if query:
        staffs=Staff.objects.filter(Q(employee_id__icontains=query) | (Q(full_name__icontains=query)
                        | Q(role__iexact=query) | Q(gender__iexact=query) | Q(subject__icontains=query)))
    else:
        staffs = Staff.objects.all()

    context={'staffs':staffs}
    return render(request,'staff/staff_list.html',context)


def add_staff(request):
    if request.method=="POST":
        form=StaffForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,'Staff Added Successfully !!')
            return redirect('all_staff_list')


    form=StaffForm()
    context={'form':form}
    return render(request,'staff/add_staff.html',context)


def edit_staff(request,pk):
    form=get_object_or_404(Staff,pk=pk)
    if request.method=="POST":
        form=StaffForm(request.POST,request.FILES,instance=form)
        if form.is_valid():
            form.save()
            messages.success(request,'Staff Updated Successfully!!')
            return redirect('all_staff_list')

    form=StaffForm(instance=form)
    context={'form':form}
    return render(request,'staff/edit_staff.html',context)


def delete_staff(request,pk):
    form=get_object_or_404(Staff,pk=pk)
    form.delete()
    messages.success(request,'Staff Deleted Successfully!!')
    return redirect('all_staff_list')


#<---------------------------------------------------------------Staff section End-------------------------->

def staff_attendance(request):
    query=request.GET.get('q')
    if query:
        staffs=StaffAttendance.objects.filter(Q(staff__full_name__icontains=query) |
                                    Q(date__icontains=query) |
                                    Q(status__icontains=query)| Q(remark__icontains=query))
    else:
        staffs=StaffAttendance.objects.all()
    context={'staffs':staffs}
    return render(request,'staff/staff_attendance.html',context)


def  add_staff_attendance(request):
    staffs_list=Staff.objects.filter(status='Active')
    today=request.GET.get('date') or timezone.now().date()

    if request.method=="POST":
        date=request.POST.get('date')

        for staff in staffs_list:
            status=request.POST.get(f"status_{staff.id}")
            remark=request.POST.get(f"remark_{staff.id}")

            if status:
                StaffAttendance.objects.update_or_create(
                    staff=staff,
                    date=date,
                    defaults={
                        'status': status,
                        'remark': remark
                    } )

        messages.success(request, "Attendance Saved Successfully")
        return redirect('add_staff_attendance')
    context = {
        'staff_list': staffs_list,
        'today': today
    }
    return render(request, 'staff/add_staff_attendance.html', context)


def edit_staff_attendance(request,pk):
    form=get_object_or_404(StaffAttendance,pk=pk)
    if request.method=="POST":
        form=StaffAttendanceForm(request.POST,instance=form)
        if form.is_valid():
            form.save()
            messages.success(request,'Staff Attendance Added Successfully!!')
            return redirect('staff_attendance')

    form=StaffAttendanceForm(instance=form)
    context={'form':form}
    return render(request,'staff/edit_staff_attendance.html',context)


def delete_staff_attendance(request,pk):
    form=get_object_or_404(StaffAttendance,pk=pk)
    form.delete()
    return redirect('staff_attendance')