from django.db import models

class cloud_cover(models.Model):
    afternoon=models.IntegerField(default=0)
class location(models.Model):
    lat=models.IntegerField(default=0)
    lon=models.IntegerField(default=0)
    tz=models.CharField(max_length=100)
    date=models.DateField()
    units=models.CharField(max_length=100)
    #relation=models.OneToOneField(cloud_cover,on_delete=models.CASCADE)
class humidity(models.Model):
    afternoon=models.IntegerField(default=0)
class precipitation(models.Model):
    total=models.IntegerField(default=0)
class temperature(models.Model):
    min=models.IntegerField()
    max=models.IntegerField()
    afternoon=models.IntegerField()
    night=models.IntegerField()
    evening=models.IntegerField()
    morning=models.IntegerField()
class pressure(models.Model):
    afternoon=models.IntegerField(default=0)
class MaxV(models.Model):
    speed=models.IntegerField()
    direction=models.IntegerField(default=0)
class wind(models.Model):
    max=models.OneToOneField(MaxV,on_delete=models.CASCADE)

