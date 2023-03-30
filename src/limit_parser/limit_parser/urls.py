from django.contrib import admin
from django.urls import include, path
from rest_framework import routers

from app import viewsets


router = routers.DefaultRouter()
router.register('fuelcards', viewsets.FuelCardViewSet)


urlpatterns = [
    path('admin/', admin.site.urls),
    path('api/', include(router.urls))
]
