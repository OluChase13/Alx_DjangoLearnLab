from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions
from django.contrib.auth import authenticate
from .serializers import UserRegistrationSerializer, LoginSerializer

class RegisterView(APIView):
    def post(self, request):
        serializer = UserRegistrationSerializer(data=request.data)
        if serializer.is_valid():
            user = serializer.save()
            token, created = Token.objects.get_or_create(user=user)
            return Response({'token': token.key}, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


class LoginView(APIView):
    def post(self, request):
        serializer = LoginSerializer(data=request.data)
        if serializer.is_valid():
            user = authenticate(
                username=serializer.validated_data['username'],
                password=serializer.validated_data['password']
            )
            if user:
                token, created = Token.objects.get_or_create(user=user)
                return Response({'token': token.key}, status=status.HTTP_200_OK)
            return Response({'error': 'Invalid credentials'}, status=status.HTTP_401_UNAUTHORIZED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

from rest_framework.decorators import api_view
from django.contrib.auth import get_user_model

User = get_user_model()

@api_view(['POST'])
def follow_user(request, user_id):
    try:
        user_to_follow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if user_to_follow == request.user:
        return Response({"detail": "You cannot follow yourself"}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.add(user_to_follow)
    return Response({"detail": "Followed successfully"}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unfollow_user(request, user_id):
    try:
        user_to_unfollow = User.objects.get(id=user_id)
    except User.DoesNotExist:
        return Response({"detail": "User not found"}, status=status.HTTP_404_NOT_FOUND)

    if user_to_unfollow == request.user:
        return Response({"detail": "You cannot unfollow yourself"}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({"detail": "Unfollowed successfully"}, status=status.HTTP_200_OK)
