import requests
from django.shortcuts import render


# Create your views here.
def about_index(request):
    profile_data = requests.get(
        "https://gist.githubusercontent.com/IMZihad21/87c7211efa951e1f10b4d4f5c89fc5d5/raw/portfolioData.json"
    ).json()
    context = {"about_data": profile_data["aboutMe"]}
    return render(request, "about/index.html", context)
