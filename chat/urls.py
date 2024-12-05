from django.urls import path, include
from django.contrib.auth.views import LoginView, LogoutView


urlpatterns = [
    path("auth/login/", LoginView.as_view
         (template_name = "chat/LoginPage.html"), name = "login-user"),
    path("auth/logout/", LogoutView.as_view(), name = "logout-user"),
]