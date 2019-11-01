from django.shortcuts import render, redirect
from .forms import VictimForm, ReminderForm
from .models import Victim, Situation
from django.contrib import messages
from django.http import JsonResponse
from django.core import serializers
import json
# Create your views here.
def map_view(request):
    database = Victim.objects.all()
    data = serializers.serialize("json", database)

    return render(request, "map_view.html", {"jsonobj": data})

def map_select(request):
   
    if request.method == "POST":

        name = request.POST['name']
        lat = request.POST['lat']
        lon = request.POST['lon']
        number = request.POST['number']
        number_2 = number
        roof = request.POST['roof']
        info = request.POST['info']
        


        
        

        if(Victim.objects.filter(number_2 = number_2).exists()):
            messages.info(request, 'There seems to already be a submission for the given phone number. Please confirm your number if this is false.')
            return render(request, "map_select.html", {"exist_flag":True})
        
        else:
            obj = Victim.objects.create(name=name, lat=lat, lon=lon, number=number, number_2=number_2, roof=roof, info = info)
            obj.save()
            return redirect("../done")

 
    messages.info(request, 'Hi')
    return render(request, "map_select.html")

