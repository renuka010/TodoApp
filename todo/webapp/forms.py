from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib.auth.models import User

from django import forms

from django.forms.widgets import PasswordInput, TextInput

# register/create a user
class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'password1', 'password2'] # fields to display

#login a user
class LoginUserForm(AuthenticationForm):
    class Meta:
        model = User
        fields = ['username', 'password'] # fields to display
    username = forms.CharField(widget=TextInput())
    password = forms.CharField(widget=PasswordInput())
