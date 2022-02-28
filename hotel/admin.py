from django.contrib import admin
from .models import User, BedRoom, Reservation

admin.site.register(BedRoom)
admin.site.register(User)
admin.site.register(Reservation)
# Register your models here.
