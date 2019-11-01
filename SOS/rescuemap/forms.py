from django import forms
from .models import Victim, Situation

class ReminderForm(forms.Form):
    
    name = forms.Textarea()
    lat = forms.FloatField()
    lon = forms.FloatField()                   
    number = forms.IntegerField()              # User's Number
    number_2 = forms.IntegerField()            # Victim's Number, need not be same as Users.
    roof = forms.BooleanField()                # Availability of Rooftop for airlift
    info = forms.CharField()  


class VictimForm(forms.ModelForm):
    class Meta:
        model = Victim
        fields = [
            'name', 
            'lat',
            'lon',
            'number',
            'number_2',
            'roof',
            'info'

        ]

#class SituationForm(forms.ModelForm):
    #class Meta:
        #model = Situation
       # pass
