# from django.shortcuts import render
from rest_framework.views import APIView
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated, AllowAny
from django.contrib.auth.models import User
from .serializers import RegisterSerializer
from rest_framework.generics import CreateAPIView
from rest_framework import status

# class RegisterView(CreateAPIView):
#     queryset = User.objects.all()
#     permission_classes = (AllowAny, )
#     serializer_class = RegisterSerializer

class RegisterView(APIView):
    permission_classes = [AllowAny, ]
    
    def post(self, request):
        serializer = RegisterSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(
                {"message": "User registrated succesfully", "user": serializer.data},
                status=status.HTTP_201_CREATED
            )
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)