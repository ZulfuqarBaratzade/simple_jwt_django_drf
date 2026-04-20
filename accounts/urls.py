from django.urls import path
from rest_framework_simplejwt.views import TokenRefreshView,TokenVerifyView
from .views import RegisterView,CustomTokenView,LogoutView,ProfileView,UpdateEmailView,ProtectedDataView


urlpatterns =[
    path('api/register/',RegisterView.as_view()),
    path('api/token/',CustomTokenView.as_view()),
    path('api/token/refresh/',TokenRefreshView.as_view()),
    path('api/token/verify/',TokenVerifyView.as_view()),
    path('api/logout',LogoutView.as_view()),
    path("api/profile/",ProfileView.as_view()),
    path("api/profile/update-email/",UpdateEmailView.as_view()),
    path("api/data/",ProtectedDataView.as_view())

]