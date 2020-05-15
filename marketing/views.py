import json
from django.shortcuts import render
from django.http import HttpResponse
from rest_framework import generics
from .serializers import MetricSerializer
from django_filters.rest_framework import DjangoFilterBackend
from django_filters import FilterSet
from django_filters import rest_framework as filters
from rest_framework.filters import OrderingFilter
from django.db.models import Sum, Count, F, FloatField, ExpressionWrapper
from django.http import JsonResponse
from .models import Metric


def performance(request):
    return HttpResponse("Hello, there")


def calculate_cpi(queryset, fields):
    field_set = list(set(fields) - set(['cpi']))
    print('field_set: ', field_set)
    qs_values = queryset.annotate(computed_cpi=ExpressionWrapper((F('spend') / F('installs')), output_field=FloatField())).values(*field_set).annotate(cpi=Sum('computed_cpi'))
    return qs_values

def sum_value(queryset, fields, sum_values):
    field_set = list(set(fields) - set(sum_values)) 
    qs_values = queryset.values(*field_set)
    for val in sum_values:
        sum_values_dict = { val: Sum(val) }
        qs_values = qs_values.annotate(**sum_values_dict)
    return qs_values


class MetricFilter(FilterSet):
    os = filters.CharFilter('os')
    channel = filters.CharFilter('channel')
    date = filters.DateFromToRangeFilter()
    installs = filters.NumberFilter('installs')
    cpi = filters.NumberFilter('cpi')
    class Meta:
        model = Metric
        fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue','cpi')


class MetricListView(generics.ListAPIView):
    queryset = Metric.objects.all()
    filter_backends = (DjangoFilterBackend, OrderingFilter)
    filter_class = MetricFilter
    ordering_fields = ('date', 'channel', 'country', 'os', 'impressions', 'clicks', 'installs', 'spend', 'revenue',)

    def get_serializer_class(self):
        return MetricSerializer

    def get_queryset(self):
        query_param = self.request.query_params
        if 'cpi_sum' in query_param:
            fields = query_param['fields'].split(',')
            return calculate_cpi(self.queryset, fields)
        if 'sum' in query_param:
            fields = query_param['fields'].split(',')
            sum_values = query_param['sum'].split(',')
            aggr_sum = sum_value(self.queryset, fields, sum_values)
            return aggr_sum
        return self.queryset
