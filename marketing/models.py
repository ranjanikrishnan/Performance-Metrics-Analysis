from django.db import models


class Metric(models.Model):
    date = models.DateField()
    channel = models.TextField()
    country = models.TextField()
    os = models.TextField()
    impressions = models.IntegerField()
    clicks = models.IntegerField()
    installs = models.IntegerField(null=True)
    spend = models.FloatField()
    revenue = models.FloatField()