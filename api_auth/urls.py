from django.urls import path

from api_auth.views import AuthToken, RegisterUserView

app_name = 'api_auth'

urlpatterns = [
    path('token', AuthToken.as_view(), name='token'),
    path('register', RegisterUserView.as_view(), name='register')
]
