from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from .models import (
	Ad, Brand, Model, Generation, Body, EngineType, BoostType,
	Drive, Broken,
	)


def create_brand(name='test_brand'):
	brand = Brand.objects.create(name=name)
	return brand

def create_model(name='test_model', brand=None):
	model = Model.objects.create(name=name, brand=brand)
	return model

def create_generation(name='test_gen', model=None):
	generation = Generation.objects.create(name=name, model=model)
	return generation

def create_body(name='test_body'):
	body = Body.objects.create(name=name)
	return body

def create_enginetype(name='test_enginetype'):
	enginetype = EngineType.objects.create(name=name)
	return enginetype

def create_boosttype(name='test_boosttype'):
	boosttype = BoostType.objects.create(name=name)
	return boosttype

def create_drive(name='test_drive'):
	drive = Drive.objects.create(name=name)
	return drive

def create_broken(name='test_broken'):
	broken = Broken.objects.create(name=name)
	return broken


# Views

class TestFilterView(TestCase):
	def test_filter_view_get_status_code(self):
		"""
        The page status is 200.
        """
		response = self.client.get(reverse('ads:filter'))
		self.assertEqual(response.status_code, 200)
	
	def test_filter_view_template_used(self):
		"""
        All necessary templates are used.
        """
		response = self.client.get(reverse('ads:filter'))

		templates = [
			'brichki/base.html',
			'ads/filter.html',
		]
		for template in templates:
			self.assertTemplateUsed(response, template)


class TestAdView(TestCase):
	@classmethod
	def setUpTestData(cls):
		cls.user = User.objects.create(
    		username='testuser', password='password',
    		)
		
		brand = create_brand()
		model = create_model(brand=brand)
		generation = create_generation(model=model)

		cls.ad = Ad.objects.create(
			brand=brand, model=model, generation=generation, 
			engine_capacity=5, mileage=5, price=5,
			author=cls.user,
		)

	def test_ad_view_get_status_code(self):
		"""
        The page status is 200.
        """
		response = self.client.get(reverse('ads:ad', kwargs={'pk':self.ad.pk}))
		self.assertEqual(response.status_code, 200)
	
	def test_ad_view_template_used(self):
		"""
        All necessary templates are used.
        """
		response = self.client.get(reverse('ads:ad', kwargs={'pk':self.ad.pk}))

		templates = [
			'brichki/base.html',
			'ads/ad.html',
		]
		for template in templates:
			self.assertTemplateUsed(response, template)


# Models

class TestBrandModel(TestCase):
	def test_str_brand(self):
		brand = create_brand()
		self.assertEqual(str(brand), 'test_brand')


class TestModelModel(TestCase):
	def test_str_model(self):
		brand = create_brand()
		model = create_model(brand=brand)
		self.assertEqual(str(model), 'test_model')


class TestGenerationModel(TestCase):
	def test_str_generation(self):
		brand = create_brand()
		model = create_model(brand=brand)
		generation = create_generation(model=model)
		self.assertEqual(str(generation), 'test_gen')


class TestBodyModel(TestCase):
	def test_str_body(self):
		body = create_body()
		self.assertEqual(str(body), 'test_body')


class TestEngineTypeModel(TestCase):
	def test_str_enginetype(self):
		enginetype = create_enginetype()
		self.assertEqual(str(enginetype), 'test_enginetype')


class TestBoostTypeModel(TestCase):
	def test_str_boosttype(self):
		boosttype = create_boosttype()
		self.assertEqual(str(boosttype), 'test_boosttype')


class TestDriveModel(TestCase):
	def test_str_drive(self):
		drive = create_drive()
		self.assertEqual(str(drive), 'test_drive')


class TestBrokenModel(TestCase):
	def test_str_broken(self):
		broken = create_broken()
		self.assertEqual(str(broken), 'test_broken')


class TestAdModel(TestCase):
	def test_str_ad(self):
		brand = create_brand()
		model = create_model(brand=brand)
		generation = create_generation(model=model)
		user = User.objects.create(username='test_user', password='password')
		
		ad = Ad.objects.create(
			brand=brand, model=model, generation=generation, 
			engine_capacity=5, mileage=5, price=5,
			author=user,
		)

		self.assertEqual(str(ad), 'test_brand, test_gen, 5, test_user')