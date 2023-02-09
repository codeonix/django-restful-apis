from django.contrib import admin
from django.urls import path, include
from . import views
from tasks.views import SchemeViewSet
from rest_framework import routers

router = routers.DefaultRouter()
router.register(r'schemes', SchemeViewSet)

urlpatterns = [
    path('all', views.all_todo),
    path('', include(router.urls))
]
