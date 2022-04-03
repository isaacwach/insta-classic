from django.urls import path, include
from . import views

app_name = "social"   


urlpatterns = [
    path("", views.homepage, name="homepage"),
    path('main', views.index, name='main'),
    path("register", views.register_request, name="register"),
    path("login", views.login_request, name="login"),
    path('profile/<username>/', views.profile, name='profile'),
    path("user_profile/<username>/", views.user_profile, name="user_profile"),
    
]