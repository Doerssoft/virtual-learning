from django.contrib import admin
from django.urls import include, path
from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='users/index.html'), name='landing-page'),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('partner/', include('contact.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),

    path('social/', include('allauth.socialaccount.urls')),
    path('account/', include('allauth.urls')),
]
