from django.test import TestCase
from django.contrib.auth.models import User
from django.urls import reverse

from ads.models import Ad, Brand, Model, Generation


def create_brand(name='test_brand'):
    brand = Brand.objects.create(name=name)
    return brand

def create_model(name='test_model', brand=None):
    model = Model.objects.create(name=name, brand=brand)
    return model

def create_generation(name='test_gen', model=None):
    generation = Generation.objects.create(name=name, model=model)
    return generation


# Views

class TestCreateUserView(TestCase):
    def test_create_user_view_get_status_code(self):
        """
        The page status is 200.
        For unauthenticated user.
        """
        response = self.client.get(reverse('users:reg'))
        self.assertEqual(response.status_code, 200)

    def test_create_user_view_template_used(self):
        """
        All necessary templates are used.
        For unauthenticated user.
        """
        response = self.client.get(reverse('users:reg'))

        templates = [
            'brichki/base.html',
            'users/reg.html',
        ]
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_create_user_view_redirect_for_authenticated_user(self):
        """
        The page redirects the authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:reg'))
        self.assertEqual(response.status_code, 302)


class TestLoginUserView(TestCase):
    def test_login_user_view_get_status_code(self):
        """
        The page status is 200.
        For unauthenticated user.
        """
        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 200)

    def test_login_user_view_template_used(self):
        """
        All necessary templates are used.
        For unauthenticated user.
        """
        response = self.client.get(reverse('users:login'))

        templates = [
            'brichki/base.html',
            'users/login.html',
        ]
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_login_user_view_redirect_for_authenticated_user(self):
        """
        The page redirects the authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:login'))
        self.assertEqual(response.status_code, 302)


class TestLogoutUserView(TestCase):
    def test_logout_user_view_redirect_for_unauthenticated_user(self):
        """
        The page redirects the unauthenticated user.
        """
        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)

    def test_logout_user_view_redirect_for_authenticated_user(self):
        """
        The page redirects the authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:logout'))
        self.assertEqual(response.status_code, 302)


class TestUserView(TestCase):
    def test_user_view_get_status_code(self):
        """
        The page status is 200.
        For authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:account'))
        self.assertEqual(response.status_code, 200)

    def test_user_view_template_used(self):
        """
        All necessary templates are used.
        For authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:account'))

        templates = [
            'brichki/base.html',
            'users/account.html',
        ]
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_user_view_redirect_for_unauthenticated_user(self):
        """
        The page redirects the unauthenticated user.
        """
        response = self.client.get(reverse('users:account'))
        self.assertEqual(response.status_code, 302)


class TestCreateAdView(TestCase):
    def test_create_ad_view_get_status_code(self):
        """
        The page status is 200.
        For authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:create_ad'))
        self.assertEqual(response.status_code, 200)

    def test_create_ad_view_template_used(self):
        """
        All necessary templates are used.
        For authenticated user.
        """
        user = User.objects.create(username='test_user', password='password')
        self.client.force_login(user)

        response = self.client.get(reverse('users:create_ad'))

        templates = [
            'brichki/base.html',
            'users/create_ad.html',
        ]
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_create_ad_view_redirect_for_unauthenticated_user(self):
        """
        The page redirects the unauthenticated user.
        """
        response = self.client.get(reverse('users:create_ad'))
        self.assertEqual(response.status_code, 302)


class TestUpdateAdView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='test_user', password='password'
            )
        cls.user_author = User.objects.create(
            username='test_author', password='password'
            )
        
        brand = create_brand()
        model = create_model(brand=brand)
        generation = create_generation(model=model)

        cls.ad = Ad.objects.create(
            brand=brand, model=model, generation=generation, 
            engine_capacity=5, mileage=5, price=5,
            author=cls.user_author,
        )

    def test_update_ad_view_get_status_code_for_author(self):
        """
        The page status is 200.
        For authenticated author-user.
        """
        self.client.force_login(self.user_author)

        response = self.client.get(reverse(
            'users:update_ad', kwargs={'pk':self.ad.pk}
            ))
        self.assertEqual(response.status_code, 200)

    def test_update_ad_view_template_used_for_author(self):
        """
        All necessary templates are used.
        For authenticated author-user.
        """
        self.client.force_login(self.user_author)

        response = self.client.get(reverse(
            'users:update_ad', kwargs={'pk':self.ad.pk}
            ))

        templates = [
            'brichki/base.html',
            'users/update_ad.html',
        ]
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_update_ad_view_get_status_code_for_non_author(self):
        """
        The page status is 302.
        For authenticated user is not the author.
        """
        self.client.force_login(self.user)

        response = self.client.get(reverse(
            'users:update_ad', kwargs={'pk':self.ad.pk}
            ))
        self.assertEqual(response.status_code, 302)


class TestDeleteAdView(TestCase):
    @classmethod
    def setUpTestData(cls):
        cls.user = User.objects.create(
            username='test_user', password='password'
            )
        cls.user_author = User.objects.create(
            username='test_author', password='password'
            )
        
        brand = create_brand()
        model = create_model(brand=brand)
        generation = create_generation(model=model)

        cls.ad = Ad.objects.create(
            brand=brand, model=model, generation=generation, 
            engine_capacity=5, mileage=5, price=5,
            author=cls.user_author,
        )

    def test_delete_ad_view_get_status_code_for_author(self):
        """
        The page status is 200.
        For authenticated author user.
        """
        self.client.force_login(self.user_author)

        response = self.client.get(reverse(
            'users:delete_ad', kwargs={'pk':self.ad.pk}
            ))
        self.assertEqual(response.status_code, 200)

    def test_delete_ad_view_template_used_for_author(self):
        """
        All necessary templates are used.
        For authenticated author user.
        """
        self.client.force_login(self.user_author)

        response = self.client.get(reverse(
            'users:delete_ad', kwargs={'pk':self.ad.pk}
            ))

        templates = [
            'brichki/base.html',
            'users/delete_ad.html',
        ]
        for template in templates:
            self.assertTemplateUsed(response, template)

    def test_delete_ad_view_get_status_code_for_non_author(self):
        """
        The page status is 302.
        For authenticated user is not the author.
        """
        self.client.force_login(self.user)

        response = self.client.get(reverse(
            'users:delete_ad', kwargs={'pk':self.ad.pk}
            ))
        self.assertEqual(response.status_code, 302)