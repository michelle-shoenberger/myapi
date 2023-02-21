from django.urls import path
from .views import DrinkViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'drinks', DrinkViewSet, basename='drink')
urlpatterns = router.urls