from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages

from .forms import ContactForm


# @login_required(login_url='login')
def contact(request):
    template_name = 'contact/partners.html'

    if request.method == 'POST':
        form = ContactForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, ("Form submission was successful."))
            return render(request, 'users/index.html')
        else:
            messages.success(request, ("Form submission was failed, please check your inputs."))

            return render(request, 'users/index.html')

    form = ContactForm()
    context = {'form': form}

    return render(request, template_name, context)