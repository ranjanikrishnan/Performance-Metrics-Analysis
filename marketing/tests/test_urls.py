from django.test import SimpleTestCase
from django.urls import reverse, resolve
from marketing.views import get_hello, MetricListView

class TestUrls(SimpleTestCase):

    def test_hello_url_resolves(self):
            url = reverse('hello')
            print(resolve(url))
            self.assertEqual(resolve(url).func, get_hello)

    def test_metrics_url_resolves(self):
            url = reverse('metrics')
            print(resolve(url))
            self.assertEqual(resolve(url).func.view_class, MetricListView)




