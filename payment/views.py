from django.shortcuts import render
from rest_framework import viewsets, mixins
from .models import Transaction
from .serializers import TransactionSerializer

# Create your views here.

class TransactionViewset(mixins.ListModelMixin, viewsets.GenericViewSet):
    queryset = Transaction.objects.all()
    serializer_class = TransactionSerializer
