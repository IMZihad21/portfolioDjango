from core.models import BaseModel
from django.db import models


class Project(BaseModel):
    """
    Project model defines project information ie: name, description, links etc.
    """

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    cover = models.URLField(max_length=200)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class ProjectLink(BaseModel):
    """
    Screenshot model for project
    """

    link_name = models.TextField(max_length=100, blank=True)
    link_url = models.URLField(max_length=200)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="links")

    def __str__(self):
        return self.link_name


class ProjectScreenshot(BaseModel):
    """
    Screenshot model for project
    """

    title = models.TextField(max_length=100, blank=True)
    image_url = models.URLField(max_length=200)
    project = models.ForeignKey(
        Project, on_delete=models.CASCADE, related_name="screenshots"
    )

    def __str__(self):
        return self.title


class ProjectTag(BaseModel):
    """
    Tags for projects
    """

    title = models.TextField(max_length=100)
    project = models.ForeignKey(Project, on_delete=models.CASCADE, related_name="tags")

    def __str__(self):
        return self.title
