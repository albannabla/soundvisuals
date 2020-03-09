from django import forms

wavetype = (('1','Sawtooth'),('2','Sine'),('3','Square'))

class soundform(forms.Form):
	# osc1 = forms.MultipleChoiceField(
	# 	required=True,
	# 	widget=forms.Select,
	# 	choices= wavetype,
	# 	)
	osc1 = forms.CharField(label='Type of Osc1')
	freq1 = forms.FloatField(label='Frequence of osc1')
	osc2 = forms.CharField(label='Type of Osc2')
	freq2 = forms.FloatField(label='Frequence of osc2')
	osc3 = forms.CharField(label='Type of Osc3')
	freq3 = forms.FloatField(label='Frequence of osc3')
