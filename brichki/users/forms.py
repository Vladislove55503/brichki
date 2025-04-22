from django import forms
from django.forms import ModelForm 
from ads.models import Ad


# Create the form class.

class AdCreateForm(ModelForm):
	class Meta:
		model = Ad
		fields = ("__all__")

class AdUpdateForm(ModelForm):
	class Meta:
		model = Ad
		fields = ("__all__")