from django.contrib import admin
from .models import Food, Household, Profile

# Register your models here.
admin.site.register(Food)
admin.site.register(Household)
admin.site.register(Profile)