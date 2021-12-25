from django import forms
from django.db.models.base import Model
from django.forms.widgets import Widget
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import complaint

class complaintForm(forms.Form):
    victims_fname = forms.CharField(required=True)
    victims_lname = forms.CharField(required=True)
    contact_no = forms.IntegerField(required=True)
    email = forms.EmailField(required=True)
    location = forms.CharField(required=True)
    subject = forms.CharField(required=True,widget=forms.Textarea)
    idproof_number = forms.CharField(required=True)
    idprooof = forms.FileField(required=True)
    image = forms.ImageField()
    vedio = forms.FileField()
    message = forms.CharField(widget=forms.Textarea)
class complaintModelForm(forms.ModelForm):
    class Meta:
        model=complaint
        fields=('victims_fname','victims_lname','contact_no','email','location','subject','idproof_number','idprooof','image','vedio','message')


class CreateUserForm(UserCreationForm):
    class Meta:
        model=User
        fields=("username","email","password1","password2")

    def __init__(self, *args, **kwargs):
        super(CreateUserForm, self).__init__(*args, **kwargs)
        self.fields['email'].widget.attrs['placeholder'] = 'Enter Email'
        self.fields['username'].widget.attrs['placeholder'] = 'Enter Username'
        self.fields['password1'].widget.attrs['placeholder'] = 'Enter Password'
        self.fields['password2'].widget.attrs['placeholder'] = 'Re-Enter password'