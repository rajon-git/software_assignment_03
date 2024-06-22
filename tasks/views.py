from django.shortcuts import render, redirect
from . import forms
from . import models

# Create your views here.
def add_task(request):
    if request.method == 'POST':
        task_forms = forms.TaskForm(request.POST)
        if task_forms.is_valid():
            task_forms.save()
            return redirect("homepage")
    else:
        task_forms = forms.TaskForm()
    return render(request,"add_task.html", {'form':task_forms})

def edit_task(request,id):
    task = models.Tasks.objects.get(pk=id)
    task_forms = forms.TaskForm(instance=task)
    if request.method == 'POST':
        task_forms = forms.TaskForm(request.POST, instance=task)
        if task_forms.is_valid():
            task_forms.save()
            return redirect('homepage')

    return render(request, 'add_task.html',{'form': task_forms})

def delete_task(request,id):
    task = models.Tasks.objects.get(pk=id)
    task.delete()
    return redirect('homepage')