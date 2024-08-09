from rest_framework import generics
from rest_framework.authentication import BasicAuthentication
from rest_framework.permissions import AllowAny, IsAuthenticated
from django.contrib.auth import login, get_user_model
from django.core.exceptions import PermissionDenied
from knox.views import (
    LoginView as KnoxLoginView,
    LogoutView as KnoxLogoutView,
    LogoutAllView as KnoxLogoutAllView,
)
from rest_framework.response import Response
from .serializers import UserSerializer, UserLoginSerializer


User = get_user_model()


class UserCreateView(generics.CreateAPIView):
    """Create a new user in the system"""

    serializer_class = UserSerializer
    permission_classes = [AllowAny]


class UserDetailView(generics.RetrieveUpdateDestroyAPIView):
    serializer_class = UserSerializer
    permission_classes = [IsAuthenticated]

    def get_object(self):
        user_id = self.kwargs.get("pk")
        if str(user_id) != str(self.request.user.id):
            raise PermissionDenied(
                "You do not have permission to access this user's details."
            )
        return self.request.user


class UserLoginView(KnoxLoginView):
    authentication_classes = [BasicAuthentication]
    permission_classes = [AllowAny]

    def post(self, request, format=None, *args, **kwargs):
        serializer = UserLoginSerializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        user = serializer.validated_data["user"]
        login(request, user)
        return super(UserLoginView, self).post(request, format=None, *args, **kwargs)


class CustomLogoutView(KnoxLogoutView):
    def get_post_response(self, request):
        return Response({"message": f"Goodbye, {request.user.name}!"}, status=200)


class CustomLogoutAllView(KnoxLogoutAllView):
    def get_post_response(self):
        return Response({"message": "All tokens have been invalidated."}, status=200)
