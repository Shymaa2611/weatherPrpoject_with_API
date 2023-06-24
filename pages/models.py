from django.db import models

class cloud_cover(models.Model):
    afternoon=models.IntegerField(default=0)
class location(models.Model):
    lat=models.IntegerField(default=0)
    lon=models.IntegerField(default=0)
    tz=models.CharField(max_length=100)
    date=models.DateField()
    units=models.CharField(max_length=100)
    relation=models.OneToOneField(cloud_cover,on_delete=models.CASCADE)
class humidity(models.Model):
    afternoon=models.IntegerField(default=0)
class precipitation(models.Model):
    total=models.IntegerField(default=0)
class temperature(models.Model):
    min=models.DecimalField(decimal_places=2,max_digits=2)
    max=models.DecimalField(decimal_places=2,max_digits=2)
    afternoon=models.DecimalField(decimal_places=2,max_digits=2)
    night=models.DecimalField(decimal_places=2,max_digits=2)
    evening=models.DecimalField(decimal_places=2,max_digits=2)
    morning=models.DecimalField(decimal_places=2,max_digits=2)

class pressure(models.Model):
    afternoon=models.IntegerField(default=0)
class MaxV(models.Model):
    speed=models.DecimalField(decimal_places=2,max_digits=2)
    direction=models.IntegerField(default=0)
class wind(models.Model):
    max=models.OneToOneField(MaxV,on_delete=models.CASCADE)
class Weather(models.Model):
    Location=models.OneToOneField(location,on_delete=models.CASCADE)
    Humidity=models.OneToOneField(humidity,on_delete=models.CASCADE)
    Precipitation=models.OneToOneField(precipitation,on_delete=models.CASCADE)
    Temperature=models.OneToOneField(temperature,on_delete=models.CASCADE)
    Pressure=models.OneToOneField(pressure,on_delete=models.CASCADE)
    Wind=models.OneToOneField(wind,on_delete=models.CASCADE)

