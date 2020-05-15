from rest_framework.serializers import ModelSerializer, SerializerMethodField, ReadOnlyField
from drf_queryfields import QueryFieldsMixin
from .models import Metric


class MetricSerializer(QueryFieldsMixin, ModelSerializer):


    class Meta:
        model = Metric
        fields = ['date','channel','country','os','impressions','clicks','installs','spend','revenue','cpi']


