import requests
from django.shortcuts import render

GITHUB_PROFILE = "https://raw.githubusercontent.com/IMZihad21/IMZihad21/main/README.md"

# Create your views here.
def HomeView(request):
    htmx_request = "X-HTMX-Request" in request.headers
    github_profile = requests.get(GITHUB_PROFILE)
    context = {"github_profile": github_profile.text, "render_navbar": not htmx_request}
    return render(request, "home/index.html", context)
