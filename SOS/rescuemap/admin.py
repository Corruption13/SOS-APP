from django.contrib import admin

# Register your models here.

from .models import Situation, Victim

admin.site.register(Situation)
admin.site.register(Victim)