from django.urls import path
from .views import RegisterView
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from django.urls import path
from .views import LostItemCreateView, FoundItemCreateView

urlpatterns = [
    path('register/', RegisterView.as_view(), name='register'),
    path('login/', TokenObtainPairView.as_view(), name='login'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('lost/', LostItemCreateView.as_view(), name='lost-item'),
    path('found/', FoundItemCreateView.as_view(), name='found-item'),
    
]

