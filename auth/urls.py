from django.urls import path

from auth.views import AuthToken, RegisterUserView


urlpatterns = [
    path('token', AuthToken.as_view(), name='token'),
    path('register', RegisterUserView.as_view(), name='register')
]
