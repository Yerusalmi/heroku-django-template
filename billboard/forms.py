from django import forms
from .models import Board


class MyModelForm(forms.ModelForm):
    class Meta:
        model = Board
        fields = {'title', 'author', 'message'}