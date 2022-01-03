from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from courses.models import Course
from django.contrib.auth.models import User
# from .forms import CreateUserForm, UpdateUserForm

from django.contrib.auth import authenticate, login, logout

# from .models import LoggedIn
# from .forms import ContactForm


# @login_required(login_url='login')
def index(request):
    template_name = 'users/index.html'
    
    latest_three_courses = Course.objects.all().order_by('-id')[:3:-1]

    return render(request, template_name, {'ltc': latest_three_courses})


# def loginpage(request):
#     if request.method == 'POST':
#         username = request.POST.get('username')
#         password = request.POST.get('password')

#         user = authenticate(request, username=username, password=password)

#         if user:
#             login(request, user)
#             x = LoggedIn.objects.create(name = request.user.username, is_logged_in = True )
#             print(x)
#             u = User.objects.all()
#             for i in u:
#                 if i.username != x.name:
#                     print(i)
#             return redirect('index')
#         else:
#             messages.warning(request, 'Username or Password are not verified')
#             return redirect('login')
#     return render(request, 'users/login.html')

def logoutpage(request):
    logout(request)
    return redirect('users:login')

# def signup(request):
#     if request.user.is_authenticated:
#         return redirect('landing-page')
#     else:
#         if request.method == "POST":
#             form = CreateUserForm(request.POST)
#             if form.is_valid():
#                 form.save()
#                 # messages.success(request, 'Registration Successful')
#                 return redirect('login')
#             # else:
#         else:
#             form = CreateUserForm()
#             # return render(request, 'users/signup.html', {'form': form})
#         return render(request, 'users/signup.html', {'form':form})


# def contact_us(request):
#     if request.method == "POST":
#         form = ContactForm(request.post)

#         if form.is_valid():
#             #send email
#             #no need to save anything
#             pass
#     else:
#         form = ContactForm()
    
#     return render(request, "")

        