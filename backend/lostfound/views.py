from django.shortcuts import render

from rest_framework.response import Response
from rest_framework.views import APIView
from rest_framework import status
from django.contrib.auth.models import User
from rest_framework_simplejwt.tokens import RefreshToken
from .serializers import UserSerializer
from rest_framework import generics
from .models import LostItem, FoundItem
from .serializers import LostItemSerializer, FoundItemSerializer
from rest_framework import generics
from .models import LostItem, FoundItem
from .serializers import LostItemSerializer, FoundItemSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            refresh = RefreshToken.for_user(user)
            return Response(
                {"refresh": str(refresh), "access": str(refresh.access_token)},
                status=status.HTTP_201_CREATED,
            )
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

class LostItemCreateView(generics.CreateAPIView):
    queryset = LostItem.objects.all()
    serializer_class = LostItemSerializer

class FoundItemCreateView(generics.CreateAPIView):
    queryset = FoundItem.objects.all()
    serializer_class = FoundItemSerializer


