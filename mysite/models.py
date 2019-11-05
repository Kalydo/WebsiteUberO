from django.contrib.auth.models import User, AbstractUser
from django.db import models

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

