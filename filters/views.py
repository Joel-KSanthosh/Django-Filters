from django.shortcuts import render
from rest_framework import viewsets
from django_filters.rest_framework import DjangoFilterBackend
from .models import GenusModel
from .myfilters import GenusFilters
from .serializers import GenusSerializer
# Create your views here.

class GenusViewset(viewsets.ModelViewSet):
    queryset = GenusModel.objects.all()
    serializer_class = GenusSerializer
    filter_backends = [DjangoFilterBackend]
    filterset_class = GenusFilters
    # filterset_fields = ['id','name']

