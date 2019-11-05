from django.contrib.auth.models import User, AbstractUser
from django.db import models
from PIL import Image


class User_from_my_db(AbstractUser):
    street = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=4, blank=True)
    plz = models.PositiveIntegerField(blank=True, default=1, null=True)
    city = models.CharField(max_length=50, blank=True)


class Profile(models.Model):
    user = models.OneToOneField(User_from_my_db, on_delete=models.CASCADE)
    image = models.ImageField(default='default.jpg', upload_to='profile_pics')

    def __str__(self):
        return f'{self.user.username} Profile'

    def save(self, *args, **kwargs):
        super().save(*args, **kwargs)

        img = Image.open(self.image.path)

        if img.height > 300 or img.width > 300:
            output_size = (300, 300)
            img.thumbnail(output_size)
            img.save(self.image.path)