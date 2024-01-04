from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    pass


class Profile(models.Model):
    user = models.OneToOneField(CustomUser,
                                on_delete=models.CASCADE,
                                related_name='profile')
    city = models.CharField(max_length=30, blank=True)
    hobby = models.CharField(max_length=50, blank=True)
    age = models.IntegerField(null=True)
    profile_pic = models.ImageField(default='default_pic.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'
