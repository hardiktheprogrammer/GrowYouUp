from django.test import TestCase,Client
from home.models import Contact
from django.urls import reverse

class TestViews(TestCase):

    def setUp(self):
        self.client=Client()
        self.index=reverse('index:index')

    def test_index_GET(self):
        response = self.client.get(self.index)
        self.assertEqual(response.status_code,200)
        self.assertTemplateUsed(response,'index/index.html')

    def test_index_POST(self):
        response = self.client.post(self.index,{'name':'Aryan',
        'company_name':'xyz','email':'aryanjainak@gmail.com','phone':'834981###4',
        'message':'msg'})
        self.assertEqual(response['name'],'Aryan')