from django.contrib import admin

from projects.models import Project, ProjectTag, ProjectScreenshot


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
    inlines = [ProjectScreenshotInline, ProjectTagInline]


# Register your models here.
admin.site.register(Project, ProjectAdmin)
