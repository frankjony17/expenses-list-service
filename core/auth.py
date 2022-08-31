from django.utils.decorators import method_decorator
from drf_yasg import openapi
from drf_yasg.utils import swagger_auto_schema
from rest_framework import status, serializers
from rest_framework.authtoken.views import ObtainAuthToken
from rest_framework.authtoken.models import Token
from rest_framework.exceptions import ValidationError, AuthenticationFailed
from rest_framework.response import Response


class AuthenticationFailedSerializer(serializers.Serializer):
    default_detail = 'Incorrect authentication credentials.'


@method_decorator(name='post', decorator=swagger_auto_schema(
    tags=['Token Authentication'],
    operation_description="This authentication scheme uses a simple token-based HTTP Authentication scheme.",
    responses={
        status.HTTP_401_UNAUTHORIZED:  openapi.Response(
            'Unauthorized', schema=openapi.Schema(type=openapi.TYPE_OBJECT, properties={
                'detail': openapi.Schema(type=openapi.TYPE_STRING, description='Incorrect authentication credentials.')
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
            return Response({'token': token.key})
        except ValidationError:
            raise AuthenticationFailed()


