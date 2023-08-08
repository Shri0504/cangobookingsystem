from django.db import models


class UserData(models.Model):
    # name=models.CharField(max_length=30)
    username = models.CharField(max_length=30)
    email = models.EmailField()
    # contact=models.CharField(max_length=20)
    password = models.CharField(max_length=30)


class carinfo(models.Model):
    carnumber = models.CharField(max_length=200)
    # carstarttime=models.DateTimeField()
    # carendtime=models.DateTimeField()
    runningdays = models.CharField(max_length=200)
    # seats = models.IntegerField()
    carstartlocation = models.CharField(max_length=200)
    carsecondlocation = models.CharField(max_length=200)
    availableSeatsStop1 = models.IntegerField(default=0)
    carthridlocation = models.CharField(max_length=200)
    availableSeatsStop2 = models.IntegerField(default=0)
    carfourthlocation = models.CharField(max_length=200)
    availableSeatsStop3 = models.IntegerField(default=0)
    carendlocation = models.CharField(max_length=200)
    availableSeatsStop4 = models.IntegerField(default=0)
    carstatus = models.CharField(max_length=200)


class stationMapping(models.Model):
    carnumber = models.CharField(max_length=200)
    runningdays = models.CharField(max_length=200)
    startLocation = models.CharField(max_length=200)
    nextLocation = models.CharField(max_length=200)
    availSeat = models.IntegerField()
    totalSeat = models.IntegerField()
    active = models.CharField(max_length=200)


# for pdf

from django.db import models


# Create your models here.

class Customer(models.Model):
    name = models.CharField(max_length=200)
    logo = models.ImageField()
    description = models.TextField()
    updated = models.DateTimeField(auto_now=True)
    created = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return str(self.name)


class User_data(models.Model):
    # name = models.CharField(max_length=200)
    # gmail = models.EmailField()
    # pss = models.CharField(max_length=200)

    carnumber = models.CharField(max_length=200)
    runningdays = models.CharField(max_length=200)
    carstartlocation = models.CharField(max_length=200)
    carsecondlocation = models.CharField(max_length=200)
    carthridlocation = models.CharField(max_length=200)
    carfourthlocation = models.CharField(max_length=200)
    carendlocation = models.CharField(max_length=200)
    carstatus = models.CharField(max_length=200)


