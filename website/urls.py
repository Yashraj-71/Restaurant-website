from django.urls import path
from django.contrib.auth import views as auth_views

from .views import home, logout_user, room_detail, signup

urlpatterns = [
    path("", home, name="home"),
    path("room/<slug:slug>/", room_detail, name="room_detail"),
    path(
        "login/",
        auth_views.LoginView.as_view(template_name="website/login.html"),
        name="login",
    ),
    path("signup/", signup, name="signup"),
    path("logout/", logout_user, name="logout"),
]
