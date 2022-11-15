from django.test import TestCase
from home.models import *
from datetime import datetime

class TestModels(TestCase):
    def setUp(self):
        self.contact= Contact.objects.create(
            name='Aryan',company_name='XYz',
            email='aryanjainak@gmail.com',phone='8349811004',
            message='Msg'
        )
