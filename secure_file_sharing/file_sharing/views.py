from django.shortcuts import render

from rest_framework import viewsets, permissions
from django.db.models import Q
from rest_framework.decorators import action
from rest_framework.response import Response
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import UserProfile, File
from .serializers import UserProfileSerializer, FileSerializer
from .permissions import IsOpsUser, IsFileOwner
from .utils import generate_verification_token
from django.core.mail import send_mail
from django.conf import settings
from rest_framework.views import APIView

class UserProfileViewSet(viewsets.ModelViewSet):
    queryset = UserProfile.objects.all()
    serializer_class = UserProfileSerializer
    permission_classes = []

    @action(detail=False, methods=['post'])
    def signup(self, request):
        username = request.data.get('username')
        email = request.data.get('email')
        password = request.data.get('password')

        if not username or not email or not password:
            return Response({'error': 'All fields are required'})

        if User.objects.filter(Q(username=username) | Q(email=email)).exists():
            return Response({'error': 'Username or email already exists'})

        User.objects.create_user(username=username, email=email, password=password)
        return Response({'message': 'Signup successful'})

    @action(detail=False, methods=['post'])
    def email_verify(self, request):
        email = request.data.get('email')

        if not email:
            return Response({'error': 'Email is required'})
        
        try:
            user_profile = User.objects.get(email=email)
        except User.DoesNotExist:
            return Response({'error': 'User does not exist'})
        
        verification_token = generate_verification_token()
        user_profile.verification_token = verification_token
        user_profile.save()

        verification_link = f'{settings.BASE_DIR}/user-profiles/verify/{verification_token}/'
        subject = 'Verify Your Email'
        message = f'Hi {user_profile.username},\nPlease click the following link to verify your email: {verification_link}'
        from_email = "rishit20csu246@ncuindia.edu"
        recipient_list = [email]

        send_mail(subject, message, from_email, recipient_list)

        return Response({'message': 'Email verification sent'})

    @action(detail=False, methods=['post'])
    def login(self, request):
        username = request.data.get('username')
        password = request.data.get('password')

        if not username or not password:
            return Response({'error': 'Both username and password are required'})

        user = authenticate(request, username=username, password=password)

        if user is not None:
            login(request, user)
            return Response({'message': 'Login successful'})
        else:
            return Response({'error': 'Invalid login credentials'}, status=Response.HTTP_401_UNAUTHORIZED)

class FileViewSet(viewsets.ModelViewSet):
    queryset = File.objects.all()
    serializer_class = FileSerializer
    permission_classes = [permissions.IsAuthenticated, IsFileOwner]

    def perform_create(self, serializer):
        # Set the user based on the current request user
        serializer.save(user=self.request.user)

    @action(detail=True, methods=['get'])
    def download(self, request, pk=None):
        # Implement file download logic here
        return Response({'download-link': '.../download-file/moiasnciaduasnduoadosnoadaosid', 'message': 'success'})