from django.urls import path
from . import views
from .views import *

urlpatterns = [
    path('', views.performance, name='performance'),
    path('metrics',MetricListView.as_view(), name='query')
]