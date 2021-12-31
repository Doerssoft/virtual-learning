from django.db import models
from django.db.models.fields import CharField
# from users.models import User
# from courses.models import Author
from django.contrib.auth.models import User
from django.core.validators import FileExtensionValidator
from virtual_learning.utils import unique_slug_generator
from django.db.models.signals import pre_save

class Course(models.Model):
    course_title = models.CharField(max_length=75)
    slug = models.SlugField(unique=True, default='', max_length=100, blank=True, null=True)
    course_picture = models.ImageField(upload_to='courses_images', blank=True, null=True)
    course_details = models.TextField(default='', blank=False, help_text='Please write a short description of the course')
    created_by = models.ForeignKey(User, on_delete=models.CASCADE, related_name = 'course_add_user')
    author = models.ForeignKey('Author', on_delete=models.CASCADE, related_name='course_author')

    def __str__(self):
        return self.course_title

def pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)


pre_save.connect(pre_save_receiver, sender = Course)


class Videos(models.Model):
    video_title = models.CharField(max_length=75)
    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='course_related_to_this_video')
    video = models.FileField(upload_to='videos_uploaded',null=True,
validators=[FileExtensionValidator(allowed_extensions=['MOV','avi','mp4','webm','mkv'])])
    video_description = models.TextField(max_length=255)

    def __str__(self):
        return str(self.course.id) + " " + self.video_title



class Author(models.Model):
    author_name = models.CharField(max_length=75)
    author_title = models.CharField(max_length=75)
    mesage_from_author = models.TextField(max_length=1000)
    about_author = models.TextField(max_length=1000)
    author_image = models.ImageField(upload_to='author_image', blank=True, null=True)
    author_fb_link = models.URLField(max_length=500)
    author_twitter_link = models.URLField(max_length=500)
    author_google_link = models.URLField(max_length=500)
    author_linkedin_link = models.URLField(max_length=500)


    def __str__(self):
        return self.author_name



class Reach(models.Model):
    form_name = models.CharField(max_length=120)
    reach_out_to_us_form_link = models.URLField(max_length=100)

    def __str__(self):
        return self.form_name