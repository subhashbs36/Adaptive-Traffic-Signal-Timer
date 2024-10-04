from django.db import models

class Lane(models.Model):
    name = models.CharField(max_length=255)
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"Lane: {self.name}"

class LaneData(models.Model):
    lane = models.ForeignKey(Lane, on_delete=models.CASCADE)
    vehicle_count = models.IntegerField(default=0)
    car_count = models.IntegerField(default=0)
    bike_count = models.IntegerField(default=0)
    truck_count = models.IntegerField(default=0)
    bus_count = models.IntegerField(default=0)
    rickshaw_count = models.IntegerField(default=0)
    red_duration = models.IntegerField(default=0)
    yellow_duration = models.IntegerField(default=3)
    green_duration = models.IntegerField(default=0)
    datetime = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Lane: {self.lane.name}, Vehicle Count: {self.vehicle_count}"
