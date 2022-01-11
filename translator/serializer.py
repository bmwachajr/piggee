from django.utils import translation
from rest_framework import serializers

class textSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, allow_blank=True, max_length=200)

class PiglatinSerializer(serializers.Serializer):
    text = serializers.CharField(required=False, allow_blank=True, max_length=200)
    translation = serializers.CharField(required=False, allow_blank=True, max_length=200)
    codec = serializers.CharField(required=False, allow_blank=True, max_length=100)

