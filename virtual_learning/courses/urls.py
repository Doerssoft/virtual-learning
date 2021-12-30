from django.urls import path

from . import views

urlpatterns = [
    path('', views.courses, name='courses'),
    path('teach/', views.teach, name='teach'),
    path('about-course/<slug:slug>/', views.ac, name='ac'),
    path('course-main/<int:id>/', views.cm, name='cm'),
]
