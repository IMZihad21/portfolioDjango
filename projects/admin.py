from django.contrib import admin

from projects.models import Project, ProjectLink, ProjectScreenshot, ProjectTag


class ProjectLinkInline(admin.StackedInline):
    model = ProjectLink
    extra = 0
    exclude = ["is_active"]


class ProjectScreenshotInline(admin.StackedInline):
    model = ProjectScreenshot
    extra = 0
    exclude = ["is_active"]


class ProjectTagInline(admin.StackedInline):
    model = ProjectTag
    extra = 0
    exclude = ["is_active"]


class ProjectAdmin(admin.ModelAdmin):
    model = Project
    inlines = [ProjectLinkInline, ProjectScreenshotInline, ProjectTagInline]


# Register your models here.
admin.site.register(Project, ProjectAdmin)
