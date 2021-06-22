from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import NewsViewset

router = DefaultRouter()

router.register(r'news', NewsViewset)

urlpatterns = [
    path('', include(router.urls))
]