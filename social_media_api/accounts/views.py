from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework.authtoken.models import Token
from rest_framework import status, permissions, generics
from django.contrib.auth import authenticate, get_user_model
from .serializers import UserRegistrationSerializer, LoginSerializer
from rest_framework.decorators import api_view

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


@api_view(['POST'])
def follow_user(request, user_id):
    user_to_follow = get_user_model().objects.get(id=user_id)
    if user_to_follow == request.user:
        return Response({"detail": "You cannot follow yourself."}, status=status.HTTP_400_BAD_REQUEST)
    
    request.user.following.add(user_to_follow)
    return Response({"detail": f"Now following {user_to_follow.username}."}, status=status.HTTP_200_OK)

@api_view(['POST'])
def unfollow_user(request, user_id):
    user_to_unfollow = get_user_model().objects.get(id=user_id)
    if user_to_unfollow == request.user:
        return Response({"detail": "You cannot unfollow yourself."}, status=status.HTTP_400_BAD_REQUEST)

    request.user.following.remove(user_to_unfollow)
    return Response({"detail": f"Unfollowed {user_to_unfollow.username}."}, status=status.HTTP_200_OK)


from rest_framework.exceptions import NotFound
from .models import CustomUser

class FollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_follow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound("User not found.")
        
        if request.user == user_to_follow:
            return Response({"detail": "You cannot follow yourself."}, status=400)
        
        request.user.following.add(user_to_follow)
        return Response({"detail": f"Now following {user_to_follow.username}"}, status=200)

class UnfollowUserView(generics.GenericAPIView):
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, user_id):
        try:
            user_to_unfollow = CustomUser.objects.get(id=user_id)
        except CustomUser.DoesNotExist:
            raise NotFound("User not found.")
        
        if user_to_unfollow not in request.user.following.all():
            return Response({"detail": "You are not following this user."}, status=400)
        
        request.user.following.remove(user_to_unfollow)
        return Response({"detail": f"Unfollowed {user_to_unfollow.username}"}, status=200)