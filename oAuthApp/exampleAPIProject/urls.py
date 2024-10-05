from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("exampleAPIApp/", include("exampleAPIApp.urls")),
    path("admin/", admin.site.urls),
]
