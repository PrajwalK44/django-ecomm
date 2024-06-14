from django.contrib.auth.forms import UserCreationForm

from .models import User, Profile
from django import forms

class CustomUserForm(UserCreationForm):
    username=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Username'}))
    
    email=forms.CharField(widget=forms.TextInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Email'}))
    password1=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Password'}))
    password2=forms.CharField(widget=forms.PasswordInput(attrs={'class':'form-control my-2', 'placeholder':'Enter Password again'}))
    class Meta:
        model=User
        fields=['username', 'email', 'password1','password2']
    
class ProfileForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = [ 'phone', 'address', 'city', 'state', 'country', 'pincode']
