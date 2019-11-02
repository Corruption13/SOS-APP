from django import forms
from .models import Victim, Situation

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
