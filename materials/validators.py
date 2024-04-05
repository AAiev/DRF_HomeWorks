from rest_framework import serializers


def validator_url(value):
    if 'youtube.com' not in value.lower():
        raise serializers.ValidationError('Некорректный адрес')
