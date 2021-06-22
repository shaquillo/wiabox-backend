from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import News
from .serializers import NewsSerializer

# Create your views here.

class NewsViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = News.objects.all()
    serializer_class = NewsSerializer
