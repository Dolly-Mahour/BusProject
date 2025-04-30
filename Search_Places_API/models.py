from django.db import models
from cities_API.models import place
from datetime import date

class search_bus_trips(models.Model):
    from_place_id = models.ForeignKey(place,on_delete=models.CASCADE,related_name='from_place_id')
    to_place_id = models.ForeignKey(place,on_delete=models.CASCADE,related_name='to_place_id')
    on_date = models.DateField(default=date.today)
    departure_time = models.TimeField(null=True,blank=True)
    arrival_time = models.TimeField(null=True,blank=True)
    bus_operator = models.CharField(max_length=255,null=True,blank=True)
    seat_prices = models.CharField(max_length=255,null=True,blank=True)
