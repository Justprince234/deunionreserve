from django.urls import path

from knox import views as knox_views
from .views import RegisterAPI, LoginAPIView, UserAPI, ChangePasswordView, UserDataList, UserDataAuth

urlpatterns = [
    path('api/register/', RegisterAPI.as_view(), name='register'),
    path('api/login/', LoginAPIView.as_view(), name='login'),
    path('api/logout/', knox_views.LogoutView.as_view(), name='logout'),
    path('api/logoutall/', knox_views.LogoutAllView.as_view(), name='logoutall'),
    path('api/user/', UserAPI.as_view(), name='user'),
    path('api/change-password/', ChangePasswordView.as_view(), name='change-password'),
    path('api/updateuser/', UserDataList.as_view()),
    path('api/updateuserauth/', UserDataAuth.as_view()),
]