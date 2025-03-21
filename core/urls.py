from django.urls import path

from .views import RegisterView, LoginView, RefreshView
from .views import protected_view

from .views import IndexView

app_name = "core"


urlpatterns = [
    path("register/", RegisterView.as_view(), name="register"),
    path("login/", LoginView.as_view(), name="login"),
    path("refresh/", RefreshView.as_view(), name="refresh"),
    path("protected/", protected_view, name="protected"),
    path("", IndexView.as_view(), name="index"),
]
