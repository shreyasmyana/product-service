from django.urls import path,include
from rest_framework.routers import DefaultRouter
from .views import CategoryViewSet, ProductViewSet

from . import views

router = DefaultRouter()
router.register(r'categories', CategoryViewSet)
router.register(r'products', ProductViewSet)

urlpatterns = [
    path("service-health", views.servicehealth, name="servicehealth"),
    path('', include(router.urls))
]