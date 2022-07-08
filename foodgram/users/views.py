from rest_framework import filters, permissions, status, viewsets
from rest_framework.decorators import action, api_view
from django.shortcuts import get_object_or_404
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import AccessToken
from . models import CustomUser
from . serializers import TokenSerializer


@api_view(['POST'])
def get_jwt_token(request):
    serializer = TokenSerializer(data=request.data)
    serializer.is_valid(raise_exception=True)
    username = serializer.validated_data.get('username')
    email = serializer.validated_data.get('email')
    user = get_object_or_404(CustomUser, username=username, email=email)
    if user:
        token = AccessToken.for_user(user)
        return Response({'token': f'{token}'}, status=status.HTTP_201_CREATED)
    
