from unicodedata import category
from django.db import models
from django.urls import reverse
from datetime import datetime, date
from django.contrib.auth.models import User


# Food Model
class Food(models.Model):
    food_name = models.CharField(max_length=50)
    category = models.CharField(max_length=50)
    expiry = models.DateField()
    count = models.IntegerField()
    food_image = models.CharField(max_length=200)
    shareable = models.BooleanField(default=False)
    user = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return f'{self.food_name} x {self.count} expires {self.expiry} shareable: {self.shareable}'
    
    def get_absolute_url(self):
        return reverse('', kwargs={'food_id': self.id})

    class Meta:
        ordering = ['-expiry']

# Household Model

class Household(models.Model):
    name = models.CharField(max_length=200)

    def __str__(self):
        return self.name

# Profile Model (Extends user model)

class Profile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    household = models.ForeignKey(Household, on_delete=models.CASCADE)
    user_image = models.CharField(
        max_length=200,
        default='https://i.imgur.com/G4NNtuW.png')

    def __str__(self):
        return f'{self.user} in {self.household}'