from django.contrib.auth.models import User
from django import forms 

class LoginForms(forms.Form):
    username =forms.CharField(label='nome usuario')
    password = forms.CharField(label='senha',widget=forms.PasswordInput)
    
# class CadastroForms(forms.ModelForm): usuario cadastro
#     username =forms.CharField(label='nome usuario')
#     password = forms.CharField(label='senha',widget=forms.PasswordInput)
#     class Meta:
#         models= User
#         fields = '__all__'