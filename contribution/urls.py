from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import ContributionView

router = DefaultRouter()

router.register(r'contribution', ContributionView)

urlpatterns = [
    path('', include(router.urls))
]