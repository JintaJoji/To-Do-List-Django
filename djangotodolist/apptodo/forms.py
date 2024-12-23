from django import forms
from.models import Task
class Todo(forms.ModelForm):
    class Meta:
        model=Task
        fields='__all__'