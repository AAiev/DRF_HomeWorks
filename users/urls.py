from django.urls import path
from rest_framework_simplejwt.views import TokenObtainPairView,TokenRefreshView

from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, PaymentListAPIView, \
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('users/token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('users/token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),

    path('users/create/', UserCreateAPIView.as_view(), name='users-create'),
    path('users/', UserListAPIView.as_view(), name='users-list'),
    path('users/<int:pk>', UserRetrieveAPIView.as_view(), name='users-get'),
    path('users/update/<int:pk>', UserUpdateAPIView.as_view(), name='users-update'),

    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),

]
