from django.test import TestCase, Client
from django.urls import reverse
from goods.models import Category, Offer, Review, User
from datetime import date
import json
from django.test import SimpleTestCase
from django.urls import reverse, resolve
from goods.views import AddOffer, Index, DetailView, MainView, AddReview

class TestViews(TestCase):

    def setUp(self):
        self.client = Client()
        User.objects.create_user('homer', 'homer@simpson.net', 'simpson')
        self.main_url = reverse('goods:main')
        self.index_url = reverse('goods:index')
        self.addoffer_url = reverse('goods:addoffer')
        self.detail_url = reverse('goods:detail', args=[0])
        self.offer1 = Offer.objects.create(
            pk = 0,
            offer_text = 'a',
            offer_title = 'a',
            offer_price = '1',
            offer_phonenumber = '86333333',
            offer_address = 'ozas',
            pub_date = date.today(),
            user = User.objects.create(
                id = '0'
            ),
            category = Category.objects.create(
                category_name = 'u',
                category_colour = 'green',
            )
        )


    def test_main_GET(self):
        response = self.client.get(self.main_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/main.html')

    def test_index_GET(self):
        response = self.client.get(self.index_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/index.html')

    def test_detail_GET(self):
        response = self.client.get(self.detail_url)

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'goods/detail.html')

    def test_addoffer_GET(self):
        response = self.client.get(self.addoffer_url)

        self.assertEqual(response.status_code, 302)
        self.assertTemplateUsed(response, 'goods/addoffer.html')
        

class TestUrls(SimpleTestCase):

    def test_addoffer_url_is_resolved(self):
        url = reverse('goods:addoffer')
        self.assertEquals(resolve(url).func, AddOffer)

    def test_index_url_is_resolved(self):
        url = reverse('goods:index')
        self.assertEquals(resolve(url).func.view_class, Index)

    def test_detailview_url_is_resolved(self):
        url = reverse('goods:detail', args=[1])
        self.assertEquals(resolve(url).func.view_class, DetailView)

    def test_main_url_is_resolved(self):
        url = reverse('goods:main')
        self.assertEquals(resolve(url).func, MainView)

    def test_addreview_url_is_resolved(self):
        url = reverse('goods:addreview', args=[1])
        self.assertEquals(resolve(url).func, AddReview)    