import requests
from django.shortcuts import render

GITHUB_PROFILE = "https://raw.githubusercontent.com/IMZihad21/IMZihad21/main/README.md"

# Create your views here.
def HomeView(request):
    github_profile = requests.get(GITHUB_PROFILE)
    context = {"github_profile": github_profile.text}
    return render(request, "home/index.html", context)
