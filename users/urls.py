from django.urls import path
from users.views import UserCreateAPIView, UserListAPIView, UserRetrieveAPIView, UserUpdateAPIView, PaymentListAPIView
from users.apps import UsersConfig

app_name = UsersConfig.name

urlpatterns = [
    path('users/create/', UserCreateAPIView.as_view(), name='users-create'),
    path('users/', UserListAPIView.as_view(), name='users-list'),
    path('users/<int:pk>', UserRetrieveAPIView.as_view(), name='users-get'),
    path('users/update/<int:pk>', UserUpdateAPIView.as_view(), name='users-update'),

    path('payment/', PaymentListAPIView.as_view(), name='payment-list'),
]
