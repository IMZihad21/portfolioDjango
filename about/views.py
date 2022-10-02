import requests
from django.shortcuts import render


# Create your views here.
def AboutView(request):
    context = {}
    return render(request, "about/about.html", context)
