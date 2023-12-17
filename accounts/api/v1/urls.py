from django.urls import path
from . import views
from rest_framework_simplejwt.views import TokenRefreshView

app_name = 'api-accounts'

urlpatterns = [
    # Register
    path('register/', views.RegisterView.as_view(), name='register'),
    # Login
    path('login/', views.LoginView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    # Change Password
    path('change-password/', views.ChangePasswordView.as_view(), name='change_password'),
    # Profile
    path('profile/', views.ProfileView.as_view(), name='profile'),
    # Logout
    path('logout/', views.LogoutView.as_view(), name='logout'),
]