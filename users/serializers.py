from rest_framework import serializers

from users.models import User


class UserSerializer(serializers.ModelSerializer):

    class Meta:
        model = User
        fields = ['pk', 'first_name', 'last_name', 'email', 'phone', 'country', 'avatar']
