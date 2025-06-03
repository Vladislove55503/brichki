from django import forms
from django.forms import ModelForm 
from ads.models import Ad


class AdCreateForm(ModelForm):
	class Meta:
		model = Ad
		fields = (
			'brand', 'model', 'generation', 'body', 'engine_type', 
			'boost_type', 'drive', 'broken', 'comment', 
			'engine_capacity', 'mileage', 'price')

class AdUpdateForm(ModelForm):
	class Meta:
		model = Ad
		fields = (
			'brand', 'model', 'generation', 'body', 'engine_type', 
			'boost_type', 'drive', 'broken', 'comment', 
			'engine_capacity', 'mileage', 'price')