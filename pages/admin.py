from django.contrib import admin
from .models import wind,precipitation,pressure,temperature,MaxV, cloud_cover,humidity,location

admin.site.register(wind)
admin.site.register(precipitation)
admin.site.register(pressure)
admin.site.register(temperature)
admin.site.register(MaxV)
admin.site.register(cloud_cover)
admin.site.register(humidity)
admin.site.register(location)