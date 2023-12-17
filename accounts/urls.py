from django.urls import path, include
from . import views

app_name = 'accounts'

urlpatterns = [
    path('login/', views.LoginUser.as_view(), name='login'),
    path('logout/', views.LogoutUser.as_view(), name='logout'),
    path('signup/', views.SignupUser.as_view(), name='signup'),
    path('api/v1/', include('accounts.api.v1.urls', namespace='v1.api.accounts')),
]
