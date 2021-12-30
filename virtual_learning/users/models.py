import uuid

from django.db import models
from django.contrib.auth.models import AbstractUser, User
from django.core.exceptions import ValidationError


def profile_pic_path(instance, filename):
	extension = filename.split('.')[1]
	if len(filename.split('.')) != 2:
		raise ValidationError("cannot load the image due to some error.")
	if extension not in ['jpg', 'jpeg']:
		raise ValidationError("we currently accept jpg/jpeg formats only.")
	unique_name = uuid.uuid4().hex
	return 'users_pictures/' + unique_name + '.' + extension


class User(AbstractUser):
	# customizing fields
	id = models.UUIDField(primary_key=True, default=uuid.uuid4)
	email = models.EmailField(verbose_name='email', max_length=256, unique=True)

	USERNAME_FIELD = 'email' 
	REQUIRED_FIELDS = ['username', 'first_name', 'last_name'] 
	# fullname
	def __str__(self):
		return self.username


class Profile(models.Model):
	user = models.OneToOneField(User, on_delete=models.CASCADE)
	id = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
	image = models.ImageField(
		default='default_pic_author.jpg',
		upload_to=profile_pic_path)
	dob = models.DateField(auto_now=False, auto_now_add=False, null=True,)

	def __str__(self):
		return f"{self.user.username}'s Profile"


class LoggedIn(models.Model):
    name = models.CharField('name', max_length=120)
    is_logged_in = models.BooleanField(blank= True, default=False)

    def __str__(self):
        return self.name