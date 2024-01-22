from django import forms
from .models import *

class signupForm(forms.ModelForm):
    class Meta:
        model=usersignup
        fields='__all__'

class notesform(forms.ModelForm):
    class Meta:
        model=mynotes
        fields='__all__'

class feedbackform(forms.ModelForm):
    class Meta:
        model=feedback
        fields='__all__'