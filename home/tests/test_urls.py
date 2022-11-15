from django.test import SimpleTestCase
from django.urls import reverse,resolve
from home.views import index

class TestUrls(SimpleTestCase):
    def test_index_url(self):
        url = reverse('index:index')
        self.assertEqual(resolve(url).func,index)