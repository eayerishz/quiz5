from django.urls import path
from . import views
from .views import UserProfileView

urlpatterns = [
    path('users/', views.get_users, name='get_users'),
    path('users/<uuid:user_uuid>/', views.get_user, name='get_user'),
    path('profile/', UserProfileView.as_view(), name='user-profile'),
    path('api/profile/', UserProfileView.as_view(), name='user_profile'),
]

