from django.shortcuts import render
from .models import Contribution
from .serializers import ContributionSerializer
from rest_framework import viewsets, mixins

# Create your views here.

class ContributionView(mixins.ListModelMixin ,viewsets.GenericViewSet):
    queryset = Contribution.objects.all()
    serializer_class = ContributionSerializer
