from django.shortcuts import render


def map_view(request):
    return render(request, "index.html")


def user_view(request):
    return render(request, "user.html")
