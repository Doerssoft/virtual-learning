from django.contrib import admin
from .models import Course, Videos, Author, Reach


# Register your models here.

admin.site.register(Course)
admin.site.register(Videos)
admin.site.register(Author)
admin.site.register(Reach)