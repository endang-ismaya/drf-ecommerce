"""
Project's URL
"""
from django.contrib import admin
from django.urls import path, include
from rest_framework.routers import DefaultRouter
from _apps.product import views

router = DefaultRouter()
router.register(r"categories", views.CategoryView)


urlpatterns = [
    path("admin/", admin.site.urls),
    path("api/", include(router.urls)),
]
