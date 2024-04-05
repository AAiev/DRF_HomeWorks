from rest_framework import serializers

from django.contrib.auth.hashers import make_password

from users.models import User, Payment, SubscribeToUpdate


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class SubscribeToUpdateSerializer(serializers.ModelSerializer):

    class Meta:
        model = SubscribeToUpdate
        fields = '__all__'


class UserRegisterSerializer(serializers.ModelSerializer):
    password = serializers.CharField(
        max_length=68, min_length=3)

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.
        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name', 'last_name', ]


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True, many=True)
    subscribe = SubscribeToUpdateSerializer(read_only=True, many=True)

    def validate_password(self, value: str) -> str:
        """
        Hash value passed by user.

        :param value: password of a user
        :return: a hashed version of the password
        """
        return make_password(value)

    class Meta:
        model = User
        fields = '__all__'


class UserListSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['first_name', 'phone',
                  'country', 'avatar',]


class UserRetrieveSerializer(UserSerializer):

    class Meta:
        model = User
        fields = ['email', 'password', 'first_name',
                  'last_name', 'payment', 'phone',
                  'country', 'avatar', 'subscribe',]
