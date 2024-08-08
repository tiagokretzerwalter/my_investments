from django.urls import path

from .views import UserCreateView, UserDetailView, UserLoginView

urlpatterns = [
    path("create/", UserCreateView.as_view(), name="user-create"),
    path("<int:pk>/", UserDetailView.as_view(), name="user-detail"),
    path("login/", UserLoginView.as_view(), name="user-login"),
]
