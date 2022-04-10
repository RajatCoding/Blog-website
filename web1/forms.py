
from django import forms
from platformdirs import user_config_dir
from .models import Post
from django.contrib.auth.forms import UserCreationForm,UserChangeForm,AuthenticationForm
from django.contrib.auth.models import User


class SignUp(UserCreationForm):
    password2 = forms.CharField(
        label='Confirm Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password1 = forms.CharField(
        label='Password', widget=forms.PasswordInput(attrs={'class':'form-control'}))    
    class Meta:
        model = User
        fields = ['first_name', 'last_name','username', 'email']
        labels = {'email': 'Email', 'first_name':'First Name','last_name':'Last Name' }
        widgets = {'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Username'}),
        'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}),
        'last_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Last Name'}),
        'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter@email'}),
        
        
        }

class Profile_Change(UserChangeForm):
    password = None
    class Meta:
        model = User
        fields = ['username', 'first_name', 'last_name', 'email', ]
        labels = {'email':'Email'}
        widgets ={'username': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Username'}),
        'first_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter First Name'}),
        'last_name': forms.TextInput(attrs = {'class':'form-control','placeholder':'Enter Last Name'}),
        'email': forms.EmailInput(attrs = {'class':'form-control','placeholder':'Enter@email'}),
        }

class AuthPost(forms.ModelForm):
    class Meta:
        model = Post
        fields = ['title', 'desc']
        labels = {'desc': 'Discription'}
        widgets = {'title': forms.TextInput(attrs={'class':'form-control'}),
                    'desc': forms.Textarea(attrs={'class':'form-control'}),
                    }
class LoginForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password']
        labels = {'username':'User Name', 'password':'Password'}
        widgets = {'username': forms.TextInput(attrs={'class':'form-control'})}