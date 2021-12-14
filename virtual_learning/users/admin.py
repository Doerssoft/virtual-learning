from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

from .forms import CreateUserForm, UpdateUserForm
from .models import User


class CustomUserAdmin(UserAdmin):
    add_form = CreateUserForm
    form = UpdateUserForm
    model = User

admin.site.register(User, CustomUserAdmin)
