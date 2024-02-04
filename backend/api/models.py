from django.db import models
from django.contrib.auth.models import BaseUserManager,AbstractUser
from django.utils import timezone
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _
import os




# Create your models here.


class UserManager(BaseUserManager):
    use_in_migrations = True
 
    def _create_user(self, email, password, **extra_fields):
        """
        Creates and saves a User with the given email and password.
        """
        if not email:
            raise ValueError('The given email must be set')
        email = self.normalize_email(email)
        user = self.model(email=email, **extra_fields)
        user.set_password(password)
        user.save(using=self._db)
        return user
 
    def create_user(self, email, password=None, **extra_fields):
        extra_fields.setdefault('is_superuser', False)
        extra_fields.setdefault('is_staff', False)
        return self._create_user(email, password, **extra_fields)
 
    def create_superuser(self, email, password, **extra_fields):
        extra_fields.setdefault('is_superuser', True)
        extra_fields.setdefault('is_staff', True)
 
        if extra_fields.get('is_superuser') is not True:
            raise ValueError('Superuser must have is_superuser=True.')
 
        return self._create_user(email, password, **extra_fields)
    
    
class User(AbstractUser):
     USER_ROLE = 'user'
  
     name = models.CharField(max_length=255)
     email = models.CharField(max_length=255, unique=True)
     password = models.CharField(max_length=255)
     username = None

     role = models.CharField(max_length=255, default=USER_ROLE)
     join_date = models.DateField(default=timezone.now)
     join_time = models.TimeField(default=timezone.now)

     USERNAME_FIELD = 'email'
     REQUIRED_FIELDS = []
     objects = UserManager



#extension_logic
def validate_file_extension(value):
    ext = os.path.splitext(value.name)[1]
    valid_extensions = ['.mp4', '.mkv']
    if not ext.lower() in valid_extensions:
        raise ValidationError(_('Unsupported file extension. Only .mp4 and .mkv files are allowed.'))

#ratio

#video_model
def upload_to(instance, filename):
    return 'videos/{filename}'.format(filename=filename)


class VideoModel(models.Model):
    video = models.FileField(upload_to=upload_to, validators=[validate_file_extension])
    description=models.TextField(max_length=255)





