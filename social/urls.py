from django.urls import path
from . import views

app_name = "social"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('user_profile/<username>/', views.user_profile, name='user_profile'),
    path('profile/<username>/', views.profile, name='profile'),
]