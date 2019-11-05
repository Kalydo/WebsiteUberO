from django.contrib.auth.models import User, AbstractUser
from django.db import models
from PIL import Image

DRIVER_CHOICES = (
    ('max', 'Max'),
    ('peter', 'Peter'),
    ('manu', 'Manu'),
    ('sebastian', 'Sebastian'),
    ('donald', 'Donald'),
)


COUNT_CHOICES = (
    ('1person', '1 Person'),
    ('2personen', '2 Personen'),
    ('3personen', '3 Personen'),
    ('4personen', '4 Personen'),
    ('5personen', '5 Personen'),
    ('6personen', '6 Personen'),
)


class User_from_my_db(AbstractUser):
    street = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=4, blank=True)
    plz = models.PositiveIntegerField(blank=True, default=1, null=True)
    city = models.CharField(max_length=50, blank=True)


<<<<<<< HEAD
class ReservationForm(models.Model):
    user = models.ForeignKey(User_from_my_db, on_delete=models.CASCADE, null=True)
    title = models.CharField(max_length=50, choices=COUNT_CHOICES, blank=True)
    ticket_number = models.IntegerField(blank=True)
    taxi_driver = models.CharField(max_length=50, choices=DRIVER_CHOICES)
    order_time = models.CharField(max_length=50, blank=True, null=True)
    from_loc = models.CharField(max_length=50, null=True)
    from_street = models.CharField(max_length=50, null=True)
    from_street_number = models.CharField(max_length=50, null=True)
    from_plz = models.PositiveIntegerField(blank=True, null=True)
    to_loc = models.CharField(max_length=50, null=True)
    to_street = models.CharField(max_length=50, null=True)
    to_street_number = models.CharField(max_length=50, null=True)
    to_plz = models.PositiveIntegerField(blank=True, null=True)

=======
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
>>>>>>> master
