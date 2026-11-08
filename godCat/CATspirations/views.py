# from django.shortcuts import render
from rest_framework import viewsets
from .models import Theocat
from .serializers import TheocatSerializer

class TheocatViewSet(viewsets.ModelViewSet):
    queryset = Theocat.objects.all()
    serializer_class = TheocatSerializer
