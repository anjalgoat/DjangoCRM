from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
from .models import Record

class SignUpForm(UserCreationForm):
    first_name= forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name' }))
    last_name= forms.CharField(label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'Last name'}))
    email= forms.EmailField(label='', widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email'}))

    class Meta:
        model = User
        fields = ('username','first_name','last_name','email','password1','password2')


#Add record form
class AddRecordForm(forms.ModelForm):
    first_name= forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'First name' }))
    last_name= forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'last name' }))
    email = forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'email ' }))
    phone = forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'phone ' }))
    address = forms.CharField(required=True, label='', max_length=50, widget=forms.TextInput(attrs={'class':'form-control', 'placeholder':'address' }))

    class Meta:
        model = Record
        exclude = ("user",)
