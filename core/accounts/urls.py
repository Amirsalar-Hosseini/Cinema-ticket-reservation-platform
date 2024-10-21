from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView
from .tokens import CustomTokenObtainPairView
from .views import UserRegisterView, UserUpdateView, UserLogOutView

app_name = 'accounts'
urlpatterns = [
    path('login/', CustomTokenObtainPairView.as_view(), name='user_login'),
    path('logout/', UserLogOutView.as_view(), name='user_logout'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]