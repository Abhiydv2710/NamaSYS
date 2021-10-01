from django.core import validators
from django import forms


class StudentRegistration(forms.Form):
    username=forms.CharField()
    email=forms.EmailField()
    password=forms.CharField(widget=forms.PasswordInput)
    ConfirmPassword=forms.CharField(widget=forms.PasswordInput)
    address=forms.CharField() 
  
    def clean(self):
        cleaned_data=super().clean()
        valpwd=self.cleaned_data['password']
        valrpwd=self.cleaned_data['ConfirmPassword']
        if valpwd!=valrpwd:
            raise forms.ValidationError('Password does not match')      


