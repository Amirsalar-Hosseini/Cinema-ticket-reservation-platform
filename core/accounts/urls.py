from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView, TokenObtainPairView
from .views import UserRegisterView, UserUpdateView

app_name = 'accounts'
urlpatterns = [
    path('api/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('api/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('register/', UserRegisterView.as_view(), name='user_register'),
    path('update/<int:pk>/', UserUpdateView.as_view(), name='user_update'),
]