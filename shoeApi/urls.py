
from rest_framework.routers import DefaultRouter
from django.urls import path, include
from .views import *

router = DefaultRouter()
router.register(r'men', MenViewSet)
router.register(r'women', WomenViewSet)
router.register(r'kids', KidsViewSet)
router.register(r'newArrivals', NewArrivalModelViewSet)

urlpatterns = [
    path('', include(router.urls)),
]