from django_filters.rest_framework import DjangoFilterBackend

from rest_framework import generics
from rest_framework.filters import OrderingFilter
from rest_framework.permissions import AllowAny, IsAdminUser

from users.models import User, Payment
from users.permissions import IsStudentOwner, IsStudentReadList
from users.serializers import UserRegisterSerializer, UserSerializer, PaymentSerializer, UserListSerializer, \
    UserRetrieveSerializer


class UserCreateAPIView(generics.CreateAPIView):
    serializer_class = UserRegisterSerializer
    permission_classes = [AllowAny]


class UserListAPIView(generics.ListAPIView):
    serializer_class = UserListSerializer
    queryset = User.objects.all()
    permission_classes = [IsStudentReadList]


class UserRetrieveAPIView(generics.RetrieveAPIView):
    queryset = User.objects.all()
    serializer_class = UserRetrieveSerializer
    permission_classes = [IsStudentOwner]


class UserUpdateAPIView(generics.UpdateAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class UserDestroyAPIView(generics.DestroyAPIView):
    serializer_class = UserSerializer
    queryset = User.objects.all()
    permission_classes = [IsAdminUser]


class PaymentListAPIView(generics.ListAPIView):
    serializer_class = PaymentSerializer
    queryset = Payment.objects.all()
    filter_backends = [DjangoFilterBackend, OrderingFilter]
    filterset_fields = ('course', 'lesson', 'method_payment')
    ordering_fields = ['date_pay']
    permission_classes = [IsAdminUser]
