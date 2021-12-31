from django.contrib import admin
from django.contrib.auth.admin import UserAdmin

# from django.contrib.auth.models import User
# from .forms import CreateUserForm, UpdateUserForm
# from .models import User


# class CustomUserAdmin(UserAdmin):
#     add_form = CreateUserForm
#     form = UpdateUserForm
#     model = User
#
#     # customizing admins dashboard STARTS
#     fieldsets = (
#         (None, {'fields': ('email', 'password', 'first_name', 'middle_name', 'last_name', 'last_login')}),
#         ('Permissions', {'fields': (
#             'is_active',
#             'is_staff',
#             'is_superuser',
#             'groups',
#             'user_permissions',
#         )}),
#     )
#     add_fieldsets = (
#         (
#             None,
#             {
#                 'classes': ('wide',),
#                 'fields': ('email', 'password1', 'password2')
#             }
#         ),
#     )
#
#     list_display = ('first_name', 'email',  'is_staff', 'last_login')
#     list_filter = ('is_staff', 'is_superuser', 'is_active', 'groups')
#     search_fields = ('email',)
#     ordering = ('email',)
#     filter_horizontal = ('groups', 'user_permissions',)
#     # customizing admins dashboard ENDS

# admin.site.register(User)
# admin.site.register(Profile)
