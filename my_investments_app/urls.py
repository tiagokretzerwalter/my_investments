from django.urls import path

from .views import CreateUserView, UpdateUserView, UserLoginView

urlpatterns = [
    path("create/", CreateUserView.as_view(), name="create"),
    path("update/", UpdateUserView.as_view(), name="update_user"),
    path("login/", UserLoginView.as_view(), name="user_login"),
]
