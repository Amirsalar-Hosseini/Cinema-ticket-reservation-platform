from django.urls import path
from .views import CinemaView, ScreenView, LocationView

app_name='cinema'
urlpatterns = [
    path('', CinemaView.as_view(), name='cinema'),
    path('screen/', ScreenView.as_view(), name='screen'),
    path('location/', LocationView.as_view(), name='location'),
]