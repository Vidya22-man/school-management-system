from django.contrib.auth.forms import AuthenticationForm
from django.shortcuts import render,redirect
from staff.models import Staff
from student.models import Student
from subject.models import Subject
from .forms import RegistrationForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib import auth


# Create your views here.





def home(request):
    total_staff = Staff.objects.count()
    total_students = Student.objects.count()
    total_subjects = Subject.objects.count()

    context = {
        'total_staff': total_staff,
        'total_subjects': total_subjects,
        'total_students': total_students}
    return render(request, 'base/home.html', context)


def register(request):
    if request.method=="POST":
        form=RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request,"Your account has been created ! you are logged in !")
            return redirect('register')
    else:
        form=RegistrationForm()

    context={'form':form}
    return render(request, 'base/register.html',context)


def login(request):
    if request.method=="POST":
        form=AuthenticationForm(request,request.POST)
        if form.is_valid():
            username=form.cleaned_data['username']
            password=form.cleaned_data['password']
            user=auth.authenticate(username=username,password=password)
            if user is not None:
                auth.login(request,user)
                messages.success(request,"You have successfully Logged In")
                return redirect('home')

    form=AuthenticationForm()
    context={'form':form}
    return render(request,'base/login.html',context)

def logout(request):
    auth.logout(request)
    return redirect('index')