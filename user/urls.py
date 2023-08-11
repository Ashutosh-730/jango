from django.urls import path
from .views import UserAPIView, AuthAPIView

urlpatterns = [
    path('', UserAPIView.as_view(), name='user-api'),
]

