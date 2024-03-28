from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User, Payment
from users.permissions import IsMemberOwnerProfile, IsMember
from users.serializers import UserRegisterSerializer, UserSerializer, PaymentSerializer, UserListSerializer, \
    UserRetrieveSerializer


class UserCreateAPIView(generics.CreateAPIView):
    """
    Создание пользователя
    """
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    """
    отображение списка пользователей
    """
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsMember]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    """
    отображение пользователя
    """
    serializer_class = UserRetrieveSerializer
    queryset = User.objects.all()
    permission_classes = [IsMemberOwnerProfile]


class UserUpdateAPIView(generics.UpdateAPIView):
    """
    обновление пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    """
    удаление пользователя
    """
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class PaymentListAPIView(generics.ListAPIView):
    """
    отображение списка платежей пользователя
    """
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method_payment')
    ordering_fields = ['date_pay']
    permission_classes = [IsAdminUser]
