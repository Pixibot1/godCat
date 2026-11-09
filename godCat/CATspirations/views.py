# from django.shortcuts import render
from rest_framework import viewsets
from rest_framework.views import APIView
from rest_framework.response import Response
from .models import Theocat
from .serializers import TheocatSerializer

# class TheocatView(APIView): # TheocatViewSet
#     def get(self, request):
#         content = Theocat.objects.all()
#         serializer = TheocatSerializer(content, many=True)
#         return Response(serializer.data)
    # queryset = Theocat.objects.all()
    # serializer_class = TheocatSerializer

class TheocatViewSet(viewsets.ModelViewSet):
    queryset = Theocat.objects.all()
    serializer_class = TheocatSerializer