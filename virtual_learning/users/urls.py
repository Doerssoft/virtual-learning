from django.urls import path

from . import views


app_name = "users"

urlpatterns = [
    path('', views.index, name='index'),
    # path('login/', views.loginpage, name='login'),
    # path('logout/', views.logoutpage, name='logout'),
    # path('signup/', views.signup, name='signup'),

    # path('pass_reset/', auth_views.PasswordResetView.as_view(template_name="user/password_reset.html"), name="reset_password"),
    # path('pass_reset_sent/', auth_views.PasswordResetDoneView.as_view(template_name="user/password_reset_sent.html"), name="password_reset_done"),
    # path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(template_name="user/password_reset_form.html"), name="password_reset_confirm"),
    # path('pass_reset_done/', auth_views.PasswordResetCompleteView.as_view(template_name="user/password_reset_completed.html"), name="password_reset_complete"),
]
