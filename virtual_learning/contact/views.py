from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.core.mail import BadHeaderError, send_mail
from django.conf import settings

from .forms import ContactForm


# @login_required(login_url='login')
def contact(request):
    template_name = 'contact/partners.html'
    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            # send email
            # no need to save them to database
            response = {}
            response["full_name"] = form.cleaned_data["full_name"]
            response["email"] = form.cleaned_data["email"]
            response["phone"] = form.cleaned_data["phone"]
            response["address"] = form.cleaned_data["address"]
            response["message"] = form.cleaned_data["message"]
            
            try:
                send_mail(
                    'Soyah --new contact message received', # subject
                    # email message/body 
                    "A new form has been recorded with following details:"+"\n"+ "\n"+
                    "Full Name: {}".format(response['full_name'])+ "\n" + 
                    "Users Email: {}".format(response['email']) + "\n" +
                    "Phone: {}".format(response['phone']) + "\n" +
                    "address: {}".format(response['address']) + "\n" +
                    "Message: {}".format(response['message']) + "\n" 
                    ,
                    settings.EMAIL_HOST_USER,  # sender
                    ['jr.gaurav2015@gmail.com'], # receiver
                    fail_silently=False,
                )
            except BadHeaderError:
                return HttpResponse('Invalid header found.')

            messages.success(request, ("Response has been recorded thank you."))
            return render(request, 'users/index.html')
        else:
            messages.success(request, ("Form submission was failed, please check your inputs."))

            return render(request, 'contact/partners.html')
    else:
        form = ContactForm()

    return render(request, template_name, {'form': form})