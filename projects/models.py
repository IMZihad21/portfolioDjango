from core.models import BaseModel
from django.contrib.postgres.fields import ArrayField
from django.db import models


class Project(BaseModel):
    """
    Project model defines project information ie: name, description, links etc.
    """

    name = models.CharField(max_length=200)
    description = models.CharField(max_length=2000)
    cover = models.CharField(max_length=200)
    screenshots = ArrayField(
        models.CharField(max_length=200),
        size=8,
    )
    tags = ArrayField(
        models.CharField(max_length=100),
        size=8,
    )
