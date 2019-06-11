from django.urls import path, include
from rest_framework_jwt.views import obtain_jwt_token

urlpatterns = [
    path('auth/login', obtain_jwt_token),
    path('indicator/', include('indicator.urls')),
]
