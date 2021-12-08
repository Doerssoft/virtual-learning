from django.urls import path

from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('teach/', views.teach, name='teach'),
    path('about-course/', views.ac, name='ac'),
    path('course-main/', views.cm, name='cm'),
]
