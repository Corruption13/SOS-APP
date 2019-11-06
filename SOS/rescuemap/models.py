from django.db import models
from django.conf import settings
from django.utils.timezone import activate

from django.contrib.auth.models import User

# Create your models here.


USER = settings.AUTH_USER_MODEL

class Victim(models.Model):

    user = models.ForeignKey(USER, default=1, on_delete=models.CASCADE, null=True)
    name = models.CharField(max_length=255, null=True, default="")
    name_2 = models.CharField(default="", null=True, max_length=255)
    address = models.TextField(default="", max_length=1000, null=True)
    lat = models.FloatField()
    lon = models.FloatField()                   
    number = models.IntegerField()              # User's Number
    number_2 = models.IntegerField(default="", null=True,)            # Victim's Number, need not be same as Users.
    roof = models.CharField(null=True, default=False, max_length=10)   # Availability of Rooftop for airlift
    info = models.TextField(null=True, default="", max_length=5000)
    total_adults = models.PositiveIntegerField(null=True, default = 1)
    total_children = models.PositiveIntegerField(null=True, default = 0)
    total_elderly = models.PositiveIntegerField(null=True, default = 0)
                       # Extra info to aid rescue team.
    inside_dz = models.BooleanField(default=True, null=True)
    time_of_creation = models.DateTimeField(null=True)
    # situation = models.ForeignKey()
  
class Situation(models.Model):
    
    name = models.CharField(max_length=255)
    c_lat = models.FloatField()                 # Center of Situation
    c_lon = models.FloatField()
    radius = models.IntegerField()              # Radius of Situation
    start_time = models.TimeField(null=True)             # Starting time of Situation
    active = models.BooleanField(default=False)

class RescueTeam(models.Model):
        user = models.ForeignKey(USER , default=1, on_delete=models.CASCADE)
        phone = models.PositiveIntegerField(null=True)
        profession = models.CharField(null=True, max_length=255)
        age = models.PositiveIntegerField(null=True)
        valid = models.BooleanField(default=False)
        # timezone = TimeZoneField(default='Asia/Kolkata')

        @classmethod
        def create(cls, user, phone, valid):
            #member = cls(user=user, phone=phone, valid=valid)
            # do something with the book
            #return member
            pass