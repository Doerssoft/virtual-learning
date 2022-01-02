from django.contrib import admin
from django.contrib import auth
from django.urls import include, path

from django.conf import settings

from django.conf.urls.static import static

from django.views.generic.base import TemplateView
from django.contrib.auth import views as auth_views
from django.conf import settings
from django.conf.urls.static import static



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', TemplateView.as_view(template_name='users/index.html'), name='landing-page'),
    path('users/', include('users.urls')),
    path('courses/', include('courses.urls')),
    path('partner/', include('contact.urls')),

    path('login/', auth_views.LoginView.as_view(template_name='users/login.html', redirect_authenticated_user=True), name='login'),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('update-password/', auth_views.PasswordChangeView.as_view(template_name='users/changepassword.html'), name='password_change'),
    path('update-password/done/', auth_views.PasswordChangeDoneView.as_view(template_name='users/passwordchangesuccess.html'), name='password_change_done'),


    path('password_reset/', auth_views.PasswordResetView.as_view(
        template_name='users/passwordreset.html'
        ), name='password_reset'),
    path('password-reset/done/', auth_views.PasswordResetDoneView.as_view(
        template_name='users/passwordresetdone.html'
        ), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(
        template_name='users/password_reset_form.html'
        ), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(
        template_name='users/passwordresetcomplete.html'
        ), name='password_reset_complete'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)