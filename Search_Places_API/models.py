from django.db import models
# from cities_API.models import place

class search_bus_trips(models.Model):
    from_place = models.CharField(max_length=255)
    to_place = models.CharField(max_length=255)
    on_date = models.DateField(null=True,blank=True)
    departure_time = models.TimeField(null=True,blank=True)
    arrival_time = models.TimeField(null=True,blank=True)
    bus_operator = models.CharField(max_length=255,null=True,blank=True)
    seat_prices = models.CharField(max_length=255,null=True,blank=True)
