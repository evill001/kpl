from django.test import SimpleTestCase
from django.urls import reverse, resolve
from django.contrib.auth import views as auth_views
from allauth.account import views as allauth_views
from . import urls

class TestUrls(SimpleTestCase):
    def test_accounts_url_resolves(self):
        url = reverse('account_login')
        self.assertEquals(resolve(url).func.view_class, allauth_views.LoginView)

    def test_admin_url_resolves(self):
        url = reverse('admin:index')
        self.assertEquals(resolve(url).func, urls.admin.site.urls)

    def test_home_url_resolves(self):
        url = reverse('home')
        self.assertEquals(resolve(url).func, urls.main)
