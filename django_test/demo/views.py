# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http.request import HttpRequest
from django.http.response import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('hello')
