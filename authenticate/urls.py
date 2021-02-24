from authenticate.views import LoginView, LogoutView, RegisterView, VerificationView
from django.urls import path

urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("activate/<uidb64>/<token>", VerificationView.as_view(), name="activate"),
    path("logout", LogoutView.as_view(), name="logout"),
]
