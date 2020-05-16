from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.get_hello, name='hello'),
    path('metrics',MetricListView.as_view(), name='metrics')
]