from rest_framework import serializers

from users.models import User, Payment


class PaymentSerializer(serializers.ModelSerializer):

    class Meta:
        model = Payment
        fields = '__all__'


class UserSerializer(serializers.ModelSerializer):
    payment = PaymentSerializer(read_only=True, many=True)

    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email', 'phone', 'country', 'avatar', 'payment']
