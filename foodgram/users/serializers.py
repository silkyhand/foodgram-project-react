from rest_framework import serializers
from . models import CustomUser


class TokenSerializer(serializers.Serializer):
    username = serializers.RegexField(required=True, regex=r'^[\w.@+-]+\Z$')
    email = serializers.EmailField(required=True, max_length=254)