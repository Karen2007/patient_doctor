from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("", include("patients.urls")),
    path("admin/", admin.site.urls),
]