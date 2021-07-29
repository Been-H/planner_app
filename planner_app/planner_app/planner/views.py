from django.http import HttpResponse, HttpResponseRedirect
from django.shortcuts import render, redirect, get_object_or_404
from django.urls import reverse, reverse_lazy
import datetime
from .models import Project, Assignment, Reminder
from .forms import CreateProjectForm, CreateAssignmentForm, CreateReminderForm

def dashboard_view(request, *args, **kwargs): 
    if request.user.is_authenticated:
        g1 = len(Project.objects.filter(user=request.user)) > 0
        context = {
            'projects' : Project.objects.filter(user=request.user),
            'countG1'  : g1
    }
        return render(request, 'dash.html', context)
    else:
        return redirect('login')

def class_view(request, id, *args, **kwargs):
    if request.user.is_authenticated:
        project = Project.objects.get(id=id)
        classPresent = len(Assignment.objects.filter(project=project)) > 0
        reminderPresent = len(Reminder.objects.filter(project=project)) > 0
        context = {
            'classPresent'     : classPresent,
            'reminderPresent'    : reminderPresent,
            'project'     : project,
            'assignments' : Assignment.objects.filter(project=project),
            'reminders'  : Reminder.objects.filter(project=project),
        }
        print(Reminder.objects.filter(project=project))
        return render(request, 'class.html', context)
    else:
        return redirect('login')

def create_class_view(request, *args, **kwargs):
    form = CreateProjectForm(request.POST or None)
    context = { 'form' : form }
    if request.user.is_authenticated:
        if request.method == 'POST':
            if request.POST.get('create') == 'Create Class':
                instance = form.save(commit=False)
                instance.user = request.user
                instance.save()
            return redirect('dashboard') 
        return render(request, 'create_class.html', context)
    else:
        return redirect('login') 

def delete_class_view(request, id, *args, **kwargs):
    if request.user.is_authenticated:
        project = Project.objects.get(id=id)
        context = {
            'item' : project
        }
        if request.method == 'POST':
            if request.POST.get('delete') == 'Delete Class':
                project.delete()
            return redirect('dashboard')
        return render(request, 'delete_class.html', context)
    else:
        return redirect('login')

def create_assignment(request, id, *args, **kwargs):
    if request.user.is_authenticated:
        form = CreateAssignmentForm()
        context = { 'form' : form }
        if request.method == 'POST':
            if request.POST.get('create') == 'Create Assignment':
                instance = Assignment()
                instance.title = request.POST.get('title')
                instance.description = request.POST.get('description')
                instance.due = request.POST.get('due')
                instance.project = Project.objects.get(id=id)
                instance.save()
            return redirect('class', id=id)
        return render(request, 'create_assignment.html', context)
    else:
        return redirect('login')

def delete_assignment(request, id, *args, **kwargs):
    assignment = Assignment.objects.get(id=id)
    class_id = assignment.project.id
    assignment.delete()
    return HttpResponseRedirect(reverse_lazy('class', kwargs={'id':class_id}))

def create_reminder(request, id, *args, **kwargs):
    if request.user.is_authenticated:
        form = CreateReminderForm()
        context = { 'form' : form }
        if request.method == 'POST':
            if request.POST.get('back') == 'Go Back':
                return redirect('class', id=id)
            instance = Reminder()
            instance.description = request.POST.get('description')
            instance.project = Project.objects.get(id=id)
            instance.save()
            return redirect('class', id=id)
        return render(request, 'create_todo.html', context)
    else:
        return redirect('login')

def delete_reminder(request, id, *args, **kwargs):
    assignment = Reminder.objects.get(id=id)
    class_id = assignment.project.id
    assignment.delete()
    return HttpResponseRedirect(reverse_lazy('class', kwargs={'id':class_id}))
