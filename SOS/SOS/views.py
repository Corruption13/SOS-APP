from django.shortcuts import render
from django.http import HttpResponse

def map_view(request):
    return render(request, "index.html")


def user_view(request):
    return render(request, "user.html")