from django.urls import path
from django.contrib.auth import views as auth_views
from . import views

app_name = "users"

urlpatterns = [
    path('users/', views.UserFormView.as_view(), name="add-user"),
    path('logout/', views.logout_user, name="logout-user"),

    # Using built-in authentication system
    path('login/', auth_views.login, {'template_name': 'users/login.html'}, name="login")
]
