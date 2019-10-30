from django.shortcuts import render, redirect
from django.http import HttpResponse

def map_view(request):
    return render(request, "map_view.html")

def map_select(request):
    return render(request, "map_select.html")

def user_view(request):
 
    if request.POST.get("rescue_me"):
        print("yes")
        return redirect("../map_me")
    elif request.POST.get("rescue_other"):  # You can use else in here too if there is only 2 submit types.
        print("no")
        return redirect("../map_other")

    return render(request, "user.html")