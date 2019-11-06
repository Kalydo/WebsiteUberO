from django.contrib import admin
from .models import Profile
from mysite.models import User_from_my_db, ReservationForm

admin.site.register(User_from_my_db)
admin.site.register(ReservationForm)
admin.site.register(Profile)

