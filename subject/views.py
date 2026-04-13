from django.shortcuts import render,redirect,get_object_or_404
from .models import Subject,Standard,Teacher
from .forms import SubjectForm,StandardForm,TeacherForm
from django.db.models import Q

# Create your views here.
def subject_list(request):
    query=request.GET.get('q')
    if query:
        subjects=Subject.objects.filter(Q(subject_name__icontains=query) |
                                        Q(code__icontains=query) |
                                         Q(standard__name__icontains=query)|
                                        Q(teacher__staff__full_name__icontains=query))
    else:
        subjects=Subject.objects.all()
    context={'subjects':subjects,}
    return render(request,'subject/subject_list.html',context)


def add_subject(request):
    if request.method=="POST":
        form=SubjectForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('subject_list')

    form=SubjectForm()
    context={'form':form}
    return render(request,'subject/add_subject.html',context)

def edit_subject(request,pk):
    form=get_object_or_404(Subject,pk=pk)
    if request.method=="POST":
        form=SubjectForm(request.POST,instance=form)
        if form.is_valid():
            form.save()
            return redirect('subject_list')

    form=SubjectForm(instance=form)
    context={'form':form}
    return render(request,'subject/edit_subject.html',context)


def delete_subject(request,pk):
    subject=get_object_or_404(Subject,pk=pk)
    subject.delete()
    return redirect('subject_list')
