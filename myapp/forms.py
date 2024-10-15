from django import forms
from .models import TodoModels
import datetime

class TodoForm(forms.ModelForm):
    due_date = forms.DateField(widget=forms.DateInput(attrs={'type': 'date'}))
    time = forms.TimeField(widget=forms.TimeInput(attrs={'type': 'time'}))

    class Meta:
        model = TodoModels
        fields = ['title', 'description', 'due_date', 'time', 'completed']
      