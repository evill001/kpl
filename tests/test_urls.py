from django.test import SimpleTestCase
from django.urls import reverse, resolve
from . import main, suvenir, kontact, reg, vhod, product_detail, cart

class TestUrls(SimpleTestCase):
    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, main)

    def test_suvenir_url_resolves(self):
        url = reverse('suvenir')
        self.assertEquals(resolve(url).func, suvenir)

    def test_kontact_url_resolves(self):
        url = reverse('kontact')
        self.assertEquals(resolve(url).func, kontact)

    def test_reg_url_resolves(self):
        url = reverse('reg')
        self.assertEquals(resolve(url).func, reg)

    def test_vhod_url_resolves(self):
        url = reverse('vhod')
        self.assertEquals(resolve(url).func, vhod)

    def test_product_detail_url_resolves(self):
        url = reverse('product_detail')
        self.assertEquals(resolve(url).func, product_detail)

    def test_cart_url_resolves(self):
        url = reverse('cart')
        self.assertEquals(resolve(url).func, cart)
