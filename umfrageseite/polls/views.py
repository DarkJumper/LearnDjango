from django.http import request
from django.http.response import HttpResponse
from django.shortcuts import render


def index(request):
    return HttpResponse("Hallo Welt")
