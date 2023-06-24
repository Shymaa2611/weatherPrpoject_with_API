from django.http import JsonResponse
from django.shortcuts import render
from .models import wind,precipitation,pressure,temperature,MaxV, cloud_cover,humidity,location



def weatherView(request):
         temp=temperature.objects.all()
         precipitn=temperature.objects.all()
         press=temperature.objects.all()
         win=wind.objects.all()
         maxv=MaxV.objects.all()
         hum=humidity.objects.all()
         loc=location.objects.all()
         clou=cloud_cover.objects.all()
         response={
            "location":list(loc.values()),
            "preciption":list(precipitn.values()),
            "pressure":list(press.values()),
            "temperature":list(press.values()),
             
        }
         return JsonResponse(response)
