from django import forms
from django.forms.widgets import Textarea
# from .models import Contact

# class ContactForm(ModelForm):

#     class Meta:
#         model = Contact
#         fields = '__all__'

class ContactForm(forms.Form):
    full_name = forms.CharField(label="Your Name", max_length=90)
    email = forms.EmailField(label="Email")
    phone = forms.IntegerField(label="Phone Number")
    address = forms.CharField(label="Address", max_length=60)
    message = forms.CharField(label="Your Message", widget=Textarea)
