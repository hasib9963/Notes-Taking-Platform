from django import forms
from .models import Note,Entry

class Noteform(forms.ModelForm):
    
    class Meta:
        model=Note
        fields=['title']
        labels={'title':'Title'}

class EntryForm(forms.ModelForm):
    class Meta:
        model=Entry
        fields=['text']
