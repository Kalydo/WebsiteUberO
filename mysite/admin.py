from django.contrib import admin
<<<<<<< HEAD
from mysite.models import User_from_my_db, ReservationForm

admin.site.register(User_from_my_db)
admin.site.register(ReservationForm)
=======
from mysite.models import User_from_my_db
from .models import Profile

admin.site.register(User_from_my_db)
admin.site.register(Profile)
>>>>>>> master
