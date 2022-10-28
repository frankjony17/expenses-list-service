from django.contrib.auth.models import User
from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import generics, status
from rest_framework.authtoken.models import Token
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.exceptions import AuthenticationFailed, ValidationError
from rest_framework.permissions import AllowAny
from rest_framework.response import Response

from api_auth.serializers import RegisterUserSerializer


@method_decorator(name='post', decorator=swagger_auto_schema(
    tags=['Authentication'],
    operation_description="This authentication scheme uses a simple token-based HTTP "
                          "Authentication scheme.",
    responses={
        status.HTTP_401_UNAUTHORIZED:  openapi.Response(
            'Unauthorized', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'detail': openapi.Schema(
                    type=openapi.TYPE_STRING, description='Incorrect authentication credentials.')
            })
        )
    }
))
class AuthToken(ObtainAuthToken):

    def post(self, request, *args, **kwargs):
        try:
            serializer = self.get_serializer(data=request.data)
            serializer.is_valid(raise_exception=True)
            user = serializer.validated_data['user']

            token, created = Token.objects.get_or_create(user=user)
            user.token = token.key
            return Response(data=RegisterUserSerializer(user).data, status=status.HTTP_200_OK)
        except ValidationError:
            raise AuthenticationFailed()


@method_decorator(name='post', decorator=swagger_auto_schema(
    tags=['Authentication'],
    operation_description="Register <b>User</b> for authentication."
))
class RegisterUserView(generics.CreateAPIView):
    queryset = User.objects.all()
    permission_classes = (AllowAny,)
    serializer_class = RegisterUserSerializer
