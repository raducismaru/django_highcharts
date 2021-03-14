from django.contrib.auth.models import AnonymousUser
from django.shortcuts import render, get_object_or_404
from raw_data import models as data_models
from raw_data.forms import PlatformForm


def home(request):
    return render(request, 'interface/home.html')
