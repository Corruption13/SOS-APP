from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from .forms import VictimForm
from .models import Victim, Situation
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
import json
from datetime import datetime
from math import sin, cos, sqrt, atan2, radians
# Create your views here.

@login_required()
def map_view(request):
    database = Victim.objects.all()
    situation = Situation.objects.all()
    data = serializers.serialize("json", database)
    data2 = serializers.serialize("json", situation)
    print(data2)

    return render(request, "map_view.html", {"jsonobj": data, "situation": data2, "user_id": request.user.first_name})

def map_select(request):
    database = Victim.objects.all()
    situation = Situation.objects.all()
    data = serializers.serialize("json", database)
    data2 = serializers.serialize("json", situation)
    try:
        user_name = request.user.first_name
    except:
        user_name = "Anonymous"

    if request.method == "POST":

        name = request.POST['name']
        lat = request.POST['lat']
        lon = request.POST['lon']
        address = request.POST['address']
        number = request.POST['number']
        number_2 = number
        roof = request.POST['roof']
        info = request.POST['info']
        total_adults = request.POST['total_adults']
        total_children = request.POST['total_children']
        total_elderly = request.POST['total_elderly']  
        name_2 = name
        
        # Distance Calculation 
        R = 6373.0                         # Approx Radius of Earth
        lat1 = radians(float(lat))
        lon1 = radians(float(lon))
        lat2 = radians(float(situation[0].c_lat))                           ## DISTANCE BETWEEN TWO GEOCOORDINATES
        lon2 = radians(float(situation[0].c_lon))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c 

        if(situation[0].radius > distance * 1000 ):
            inside_dz = True
        else:
            inside_dz = False
        

        if(Victim.objects.filter(number_2 = number_2).exists()):
            messages.info(request, 'There seems to already be a submission for the given phone number. Please confirm your number if this is false.')
            return render(request, "map_select.html", {"exist_flag":True, "jsonobj": data, "situation": data2, "user_id": user_name})
        
        else:
            obj = Victim.objects.create(
                name=name, 
                name_2 = name_2, 
                lat=lat, lon=lon, 
                address=address, 
                number=number, 
                number_2=number_2, 
                roof=roof, 
                info = info,
                total_children = total_children, 
                total_adults = total_adults, 
                total_elderly=total_elderly, 
                inside_dz = inside_dz, 
                time_of_creation = datetime.now()
                )
                
            obj.save()
            return redirect("../done")

 
  
    return render(request, "map_select.html", {"jsonobj": data, "situation": data2, "user_id": user_name})



def map_select_2(request):
    database = Victim.objects.all()
    situation = Situation.objects.all()
    data = serializers.serialize("json", database)
    data2 = serializers.serialize("json", situation)
    if request.method == "POST":

        name = request.POST['name']
        name_2 = request.POST['name_2']
        lat = request.POST['lat']
        lon = request.POST['lon']
        address = request.POST['address']
        number = request.POST['number']
        number_2 = request.POST['number_2']
        roof = request.POST['roof']
        info = request.POST['info']
        total_adults = request.POST['total_adults']
        total_children = request.POST['total_children']
        total_elderly = request.POST['total_elderly']  

        #print(situation[0].name)
        R = 6373.0
        lat1 = radians(float(lat))
        lon1 = radians(float(lon))
        lat2 = radians(float(situation[0].c_lat))
        lon2 = radians(float(situation[0].c_lon))
        dlon = lon2 - lon1
        dlat = lat2 - lat1
        a = sin(dlat / 2)**2 + cos(lat1) * cos(lat2) * sin(dlon / 2)**2
        c = 2 * atan2(sqrt(a), sqrt(1 - a))
        distance = R * c 

        if(situation[0].radius > distance * 1000 ):
            inside_dz = True
        else:
            inside_dz = False
        

        if(Victim.objects.filter(number_2 = number_2).exists()):
            messages.info(request, 'There seems to already be a submission for the given phone number. Please confirm your number if this is false.')
            return render(request, "map_select2.html", {"exist_flag":True, "jsonobj": data, "situation": data2, "user_id": request.user.first_name})
        
        else:
            obj = Victim.objects.create(
                name=name_2, 
                name_2=name, 
                lat=lat, 
                lon=lon, 
                address=address, 
                number=number, 
                number_2=number_2, 
                roof=roof, 
                info = info,
                total_children = total_children,
                total_adults = total_adults, 
                total_elderly=total_elderly, 
                inside_dz = inside_dz, time_of_creation = datetime.now()
                )
            obj.save()
            return redirect("../done")

 
  
    return render(request, "map_select2.html", {"jsonobj": data, "situation": data2})
