from django.contrib import admin
from django.urls import path, include
from .views import UserRegistration,CustomTokenObtainPairView,UserLogin

urlpatterns = [
    path('register/',UserRegistration.as_view(), name='register'),
    path('token/',CustomTokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('login/', UserLogin.as_view(), name='login')
    
]
