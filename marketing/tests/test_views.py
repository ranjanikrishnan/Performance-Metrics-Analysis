import json
from django.test import TestCase, Client
from django.urls import reverse
from marketing.models import Metric


class TestViews(TestCase):
    def setUp(self):
        self.client = Client()
        self.hello_url = reverse('hello')
        self.pk = 10000
        self.us_data = { 'id': self.pk, 'date': '2017-5-17', 'channel': 'adcolony', 'country': 'US', 'os': 'android', 'impressions': 19887, 'clicks': 494, 'installs': 76, 'spend': 148.2, 'revenue': 149.04 }
        out = Metric.objects.create(**self.us_data)
        print('out', out)

    def test_get_hello_GET(self):
        response = self.client.get(self.hello_url)

        self.assertEqual(response.status_code, 200)
        self.assertEqual(response.content, b'Hello, there')
 
    def test_metric_list_GET(self):
        url = reverse('metrics')
        got = Metric.objects.get(pk=self.pk)
        self.assertEquals('US', got.country)
        self.assertEquals('android', got.os)
        
