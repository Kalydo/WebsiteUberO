from django.contrib import admin
from mysite.models import User_from_my_db
from .models import Profile

admin.site.register(User_from_my_db)
admin.site.register(Profile)
