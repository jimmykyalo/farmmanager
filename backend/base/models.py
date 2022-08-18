from statistics import quantiles
from unicodedata import category
from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class PlantCategory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=1000, unique=True)
    

class Plant(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=1000, unique=True)
    scientificName = models.CharField(max_length=1000, unique=True, blank=True, null=True)
    category = models.CharField(max_length=1000, blank=True, null=True)
    description = models.TextField(blank=True, null=True)

class FarmInput(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=1000, unique=True)
    category = models.CharField(max_length=1000, blank=True, null=True)
    harmful = models.BooleanField(default=False)
    safety_interval = models.IntegerField()
    safety_interval_units = models.CharField(max_length=1000, blank=True, null=True)

class Activity(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.AutoField(primary_key=True, editable=False)
    name = models.CharField(max_length=1000, unique=True)

class ActivitySchedule(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    _id = models.AutoField(primary_key=True, editable=False)
    plant = models.ForeignKey(Plant, on_delete=models.CASCADE)
    activity = models.ForeignKey(Activity, on_delete=models.CASCADE)
    frequency = models.IntegerField()
    frequency_units = models.CharField(max_length=1000, blank=True, null=True)
    startDate = models.DateTimeField(blank=True, null=True)
    endDate = models.DateTimeField(blank=True, null=True)
    quantity = models.DecimalField(blank=True, null=True, decimal_places=2)
    units = models.CharField(max_length=1000, blank=True, null=True)
