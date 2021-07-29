from django.forms import ModelForm
from django import forms
from .models import Project, Assignment, Reminder

class CreateProjectForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True

    class Meta:
        model = Project
        fields = ['title']

class CreateAssignmentForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['title'].required = True
        self.fields['description'].required = True
    
    class Meta:
        model = Assignment
        fields = ['title', 'description', 'due']

class CreateReminderForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['description'].required = True
    
    
    class Meta:
        model = Reminder
        fields = ['description']
