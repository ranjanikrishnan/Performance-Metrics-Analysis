from django.shortcuts import render
from django.http import HttpResponse


def performance(request):
    return HttpResponse("Here , we analyze performance metrics.")