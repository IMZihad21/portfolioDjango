from django.urls import path

from about import views

urlpatterns = [
    path("", views.AboutView, name="about_index"),
]
