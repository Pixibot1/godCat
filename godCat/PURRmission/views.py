# from django.shortcuts import render
# from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated

class AuthUser(viewsets.ModelViewSet):
    permission_classes = (IsAuthenticated,)
    
    def list(self, request):
        content = {'message': 'WOWOWO'}
        return Response(content)
