from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


urlpatterns = [
    path('authapp/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('authapp/token/refresh/', TokenRefreshView.as_view(),
         name='token_refresh_pair'),
    path('authapp/token/verify/', TokenVerifyView.as_view(),
         name='token_verify_pair'),
]
