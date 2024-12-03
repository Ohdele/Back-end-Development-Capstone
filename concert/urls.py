from django.urls import path, re_path
from . import views

urlpatterns = [
    re_path(r"^$", views.index, name="index"),
    path("songs/", views.songs, name="songs"),
    path("photos/", views.photos, name="photos"),
    path("login/", views.login_view, name="login"),
    path("logout/", views.logout_view, name="logout"),
    path("signup/", views.signup, name="signup"),
    path("concert/", views.concerts, name="concerts"),

]
