from django.contrib import admin
from .models import Rent, Rented

# Register your models here.
admin.site.register(Rent)
admin.site.register(Rented)