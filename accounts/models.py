from django.db import models
from django.contrib.auth.models import AbstractUser
from django.urls import reverse
from PIL import Image

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

    def get_absolute_url(self):
        return reverse('profile_detail', kwargs={'pk': self.pk})

    def save(self):
        super().save()
        pic = Image.open(self.profile_pic.path)

        if pic.height > 200 or pic.width > 200:
            output_size = (200, 200)
            pic.thumbnail(output_size)
            pic.save(self.profile_pic.path)