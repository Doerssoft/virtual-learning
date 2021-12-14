from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import  forms
from .models import User

class CreateUserForm(UserCreationForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'password1', 'password2']


class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'full_name']
