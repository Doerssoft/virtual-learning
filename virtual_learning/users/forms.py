# from django.contrib.auth.forms import UserChangeForm, UserCreationForm
from django import  forms
from django.forms.widgets import Textarea
# from .models import User


# class CreateUserForm(UserCreationForm):
#     class Meta:
#         model = User
#         fields = ['first_name', 'last_name', 'username', 'email', 'password1', 'password2']


# class UpdateUserForm(UserChangeForm):
#     class Meta:
#         model = User
#         fields = ['email', 'first_name', 'last_name']


# class ContactForm(forms.Form):
#     full_name = forms.CharField(label="Your Name", max_length=90)
#     email = forms.EmailField(label="Email")
#     phone = forms.IntegerField(label="Phone Number")
#     address = forms.CharField(label="Address", max_length=60)
#     message = forms.CharField(label="Your Message", widget=Textarea)
