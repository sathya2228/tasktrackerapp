from django import forms
from .models import Task

class TaskForm(forms.ModelForm):
    class Meta:
        model = Task
        fields = ['title', 'description', 'due_date']  # Don't include progress here
        widgets = {
            'due_date': forms.DateTimeInput(attrs={'type': 'datetime-local'}),
        }

    def save(self, commit=True):
        # Add the default progress value before saving
        task = super().save(commit=False)
        if not task.progress:
            task.progress = 'in_progress'  # Default to 'in_progress' if not set
        if commit:
            task.save()
        return task
