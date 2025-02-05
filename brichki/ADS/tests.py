# from django.test import SimpleTestCase

from django.test import TestCase

from ADS.models import Ads, Comments
from FILTER.models import (
    Brand,
    Model,
    Generation,
    Body,
    EngineType,
    BoostType,
    Drive,
    Broken,
)


def create_filter_brand(pk=1, name='any'):
    brand = Brand.objects.create(
        pk=pk,
        name=name,
    )

def create_filter_model(pk=1, name='any', brand_id=1):
    model = Model.objects.create(
        pk=pk,
        brand=Brand.objects.get(pk=brand_id),
        name=name,
    )

def create_filter_generation(pk=1, name='any', model_id=1):
    generation = Generation.objects.create(
        pk=pk,
        model=Model.objects.get(pk=model_id),
        name=name,
    )

def create_filter_body(pk=1, name='any'):
    body = Body.objects.create(pk=pk, name=name)

def create_filter_engine_type(pk=1, name='any'):
    engine_type = EngineType.objects.create(pk=pk, name=name)

def create_filter_boost_type(pk=1, name='any'):
    boost_type = BoostType.objects.create(pk=pk, name=name)

def create_filter_drive(pk=1, name='any'):
    drive = Drive.objects.create(pk=pk, name=name)

def create_filter_broken(pk=1, name='any'):
    broken = Broken.objects.create(pk=pk, name=name)

def create_filter_comment(pk=1, text='any'):
    comment = Comments.objects.create(pk=pk, text=text)

def create_ad(
        brand_pk=1,
        model_pk=1,
        generation_pk=1,
        body_pk=1,
        engine_type_pk=1,
        boost_type_pk=1,
        drive_pk=1,
        broken_pk=1,
        comment_pk=1,
):
    create_filter_brand()
    create_filter_model()
    create_filter_generation()
    create_filter_body()
    create_filter_engine_type()
    create_filter_boost_type()
    create_filter_drive()
    create_filter_broken()
    create_filter_comment()

    ad = Ads.objects.create(
        pk=1,
        brand=Brand.objects.get(pk=brand_pk),
        model=Model.objects.get(pk=model_pk),
        generation=Generation.objects.get(pk=generation_pk),
        body=Body.objects.get(pk=body_pk),
        engine_type=EngineType.objects.get(pk=engine_type_pk),
        boost_type=BoostType.objects.get(pk=boost_type_pk),
        drive=Drive.objects.get(pk=drive_pk),
        broken=Broken.objects.get(pk=broken_pk),
        comment=Comments.objects.get(pk=comment_pk),
        engine_capacity=0,
        mileage=0,
        price=0,
    )


class MainPageViewTests(TestCase):
    def test_view_status_code(self):
        create_filter_engine_type(pk=4, name='Электро')
        response = self.client.get('')
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        create_filter_engine_type(pk=4, name='Электро')
        response = self.client.get('')

        templates = [
            'brichki/base.html',
            'ADS/main_page.html',
            'ADS/includes/filter_main.html',
            'ADS/includes/ads_main.html',
        ]

        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_view_template_not_used(self):
        create_filter_engine_type(pk=4, name='Электро')
        response = self.client.get('')

        templates = [
            'ADS/ad_page.html',
            'ADS/includes/card_ad.html',
        ]

        for template in templates:
            self.assertTemplateNotUsed(response, template)

    def test_not_contains(self):
        create_filter_engine_type(pk=4, name='Электро')
        create_ad(engine_type_pk=4)
        response = self.client.get('')

        texts = [
            '<span id="item-boost" class="parameter-ad">',
            '<span id="item-capacity" class="parameter-ad">',
        ]

        for text in texts:
            self.assertNotContains(
            response,
            text=text,
            status_code=200,
            )


class AdPageViewTests(TestCase):
    def test_view_status_code(self):
        create_ad()
        response = self.client.get('/1')
        self.assertEqual(response.status_code, 200)

    def test_view_template_used(self):
        create_ad()
        response = self.client.get('/1')

        templates = [
            'brichki/base.html',
            'ADS/ad_page.html',
            'ADS/includes/card_ad.html',
        ]

        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_view_template_not_used(self):
        create_ad()
        response = self.client.get('/1')

        templates = [
            'ADS/main_page.html',
            'ADS/includes/filter_main.html',
            'ADS/includes/ads_main.html',
        ]

        for template in templates:
            self.assertTemplateNotUsed(response, template)