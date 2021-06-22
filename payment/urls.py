from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import TransactionViewset

router = DefaultRouter()

router.register(r'transaction', TransactionViewset)

urlpatterns = [
    path('', include(router.urls))
]