from django.db import models
from django.db.models.base import Model

# Create your models here.
class Heroes (models.Model):
    
    super_hero_name = models.CharField(max_length=50)
    alter_ego = models.CharField(max_length=50)
    primary_power = models.CharField(max_length=50)
    secondary_power = models.CharField(max_length=50)
    catchphrase = models.CharField(max_length=50)
    
    def __str__(self):
        return self.super_hero_name
