from django.shortcuts import render
from rest_framework.views import APIView
from . import serializers
from . import models
from rest_framework.response import Response
from django.contrib.auth import authenticate
from rest_framework.exceptions import AuthenticationFailed
from rest_framework import viewsets,status
from rest_framework.parsers import FileUploadParser
from rest_framework import generics


# Create your views here.

#User_registration
class RegisterView(APIView):
    def post(self,request):
        serializer=serializers.UserSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)
    

class LoginView(APIView):
    def post(self,request):
        email=request.data.get('email')
        password=request.data.get('password')
         # Use Django's built-in authentication system
        user = authenticate(username=email, password=password)
        if user is None:
            raise AuthenticationFailed('Incorrect email or password!')
        # You can return a simple success message or user data
        return Response({
            'message': 'Login successful',
            'user_id': user.id,
            'email': user.email
            # You can add more user details here if needed
        })
            
    
#video
class VideoModelViewSet(viewsets.ModelViewSet):
    queryset = models.VideoModel.objects.all()
    serializer_class = serializers.VideoModelSerializer
    parser_classes = (FileUploadParser,)

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)

        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    

#getting all videos
class VideoListAPIView(generics.ListAPIView):
    queryset = models.VideoModel.objects.all()
    serializer_class = serializers.VideoModelSerializer    