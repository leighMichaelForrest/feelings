from django import forms

from . import models

class ThoughtForm(forms.ModelForm):
    class Meta:
        model = models.Thought
        fields = ['condition', 'notes']
