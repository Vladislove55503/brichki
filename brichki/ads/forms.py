from django import forms
from django.forms import ModelForm 
from .models import Ad


# Create the form class.

class FilterForm(ModelForm):
	class Meta:
		model = Ad
		fields = (
			'brand', 'model', 'generation', 'body', 'engine_type', 
			'boost_type', 'drive', 'broken',
			)

	def __init__(self, *args, **kwargs):
		super(FilterForm, self).__init__(*args, **kwargs)
		self.fields['brand'].required = False
		self.fields['model'].required = False
		self.fields['generation'].required = False
		self.fields['body'].required = False
		self.fields['engine_type'].required = False
		self.fields['boost_type'].required = False
		self.fields['drive'].required = False
		self.fields['broken'].required = False