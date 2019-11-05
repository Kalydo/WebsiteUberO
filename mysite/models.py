from django.contrib.auth.models import User, AbstractUser
from django.db import models


class User_from_my_db(AbstractUser):
    street = models.CharField(max_length=50, blank=True)
    street_number = models.CharField(max_length=4, blank=True)
    plz = models.PositiveIntegerField(blank=True, default=1, null=True)
    city = models.CharField(max_length=50, blank=True)


