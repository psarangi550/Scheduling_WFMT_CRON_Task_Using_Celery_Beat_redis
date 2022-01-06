from django import forms
from .models import Test_Email_Schedule

class EmailForm(forms.ModelForm):
    class Meta:
        model=Test_Email_Schedule
        fields="__all__"
        
