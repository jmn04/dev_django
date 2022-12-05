from django import forms
from .models import NoteTable

class NoteForm(forms.ModelForm):
    class Meta:
        model = NoteTable
        fields = ('title', 'text', 'image')