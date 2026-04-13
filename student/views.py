from django.shortcuts import render,redirect,get_object_or_404
from .models import Student, Father
from .forms import StudentForm,FatherForm
from django.db.models import Q
from django.contrib import messages

# Create your views here.
def all_students(request):
    query=request.GET.get('q')
    if query:
        students=Student.objects.filter(Q(first_name__icontains=query) | Q(last_name__icontains=query) | Q(father__father_name__icontains=query)).distinct()
    else:
        students=Student.objects.all()

    total_students=Student.objects.count()
    context={'students':students,'total_students':total_students}
    return render(request,'student/student_list.html',context)


def add_student(request):
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Successfully Added !!")
            return redirect('all_students')


    form=StudentForm()
    context={'form':form}
    return render(request,'student/add_student.html',context)




def edit_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    if request.method=="POST":
        form=StudentForm(request.POST,request.FILES,instance=student)
        if form.is_valid():
            form.save()
            messages.success(request,"Student Successfully Updated !!")
            return redirect('all_students')

    form=StudentForm(instance=student)
    context={'form':form}
    return render(request,'student/edit_student.html',context)

def delete_student(request,pk):
    student=get_object_or_404(Student,pk=pk)
    student.delete()
    messages.success(request,"Student Successfully Deleted !!")
    return redirect('all_students')
