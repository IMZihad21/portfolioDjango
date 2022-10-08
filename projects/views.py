from django.shortcuts import render

from projects.models import Project


# Create your views here.
def projects_index(request):
    projects = Project.objects.all()

    context = {"projects": projects}
    return render(request, "projects/index.html", context)
