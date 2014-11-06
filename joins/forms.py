from django import forms

from .models import join

class EmailForm(forms.Form):
	name = forms.CharField(required = False)
	email = forms.EmailField()

class joinForm(forms.ModelForm):
	class Meta:
		model = join