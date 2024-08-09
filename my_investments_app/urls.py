from django.urls import path

from .views import (
    UserCreateView,
    UserDetailView,
    UserLoginView,
    CustomLogoutView,
    CustomLogoutAllView,
)

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("login/", UserLoginView.as_view(), name="user-login"),
    path("logout/", CustomLogoutView.as_view(), name="user-logout"),
    path("logoutall/", CustomLogoutAllView.as_view(), name="user-logoutall"),
]
