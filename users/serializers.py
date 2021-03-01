from rest_framework import serializers


class CustomUserSerializer(serializers.Serializer):
    email = serializers.CharField(max_length=120)
    is_staff = serializers.CharField()
