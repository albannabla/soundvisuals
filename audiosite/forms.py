from django import forms
#from .models import types 

wavetype = (("Sine","Sine"),("Sawtooth","Sawtooth"),("Square","Square"),)

class soundform(forms.Form):
	osc1 = forms.MultipleChoiceField(choices = wavetype)
	freq1 = forms.FloatField(label='Frequence of osc1')
	osc2 = forms.MultipleChoiceField(choices = wavetype)
	freq2 = forms.FloatField(label='Frequence of osc2')
	osc3 = forms.MultipleChoiceField(choices = wavetype)
	freq3 = forms.FloatField(label='Frequence of osc3')
