from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import contact, blogs
from django.contrib.auth.forms import AuthenticationForm


class contact_form(forms.ModelForm):
    email = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'email'}),label=("Email"),required=True)
    address = forms.CharField(max_length=200,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'address'}),label=("Address"),required=True)
    city = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'city'}),label=("City"),required=True)
    comments = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'comments'}),label=("Comments"),required=True)
    
    class Meta: 
        model = contact
        fields = ['email', 'address', 'city', 'comments']

        
class signup_form(UserCreationForm):
    first_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'first name'}),label=("First Name"),required=True)
    last_name = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'last name'}),label=("Last Name"),required=True)
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),label=("Username"),required=True)
    email = forms.CharField(max_length=100,widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email'}),label=("Email"),required=True)
    age = forms.IntegerField(widget=forms.NumberInput(attrs={'class':'form-control','placeholder':'age'}),label=('Age'))
    password1 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label=("Password"))
    password2 = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'again password'}),label=("Password Confirmation"))
    class Meta:
        model = User
        fields = ('username','first_name','last_name','email', 'age', 'password1','password2')


class login_form(AuthenticationForm):
    username = forms.CharField(max_length=100,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'username'}),label=("Username"),required=True)
    password = forms.CharField(max_length=100,widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password'}),label=("Password"),required=True)


class blogs_form(forms.ModelForm):
    title = forms.CharField(max_length=500,widget=forms.TextInput(attrs={'class':'form-control','placeholder':'title'}),label=("Title"),required=True)
    description = forms.CharField(max_length=1000,widget=forms.Textarea(attrs={'class':'form-control','placeholder':'description'}),label=("Description"),required=True)
    class Meta:
        model = blogs
        fields = ('title', 'description')
    

