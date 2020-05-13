from django.urls import path
from . import views

urlpatterns = [
    path('', views.performance, name='performance'),
    path('data',views.load_data, name='data')
]