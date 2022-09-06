
from django.urls import include, path, re_path
from drf_yasg import openapi
from drf_yasg.views import get_schema_view
from rest_framework import permissions

app_name = 'api'
API_V1 = "api/v1"

schema_view = get_schema_view(
    openapi.Info(
        title="Expenses Shopping List",
        default_version='v1',
        description="The Smart Expenses and Shopping List App",
        # terms_of_service="https://www.google.com/policies/terms/",
        contact=openapi.Contact(email="frankjony17@gmail.com"),
        license=openapi.License(name="GNU GENERAL PUBLIC LICENSE"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

urlpatterns = [
    # Swagger UI.
    re_path(
        r'^swagger-ui(?P<format>\.json|\.yaml)$',
        schema_view.without_ui(cache_timeout=0), name='schema-json'),
    re_path(
        r'^swagger-ui/$',
        schema_view.with_ui('swagger', cache_timeout=0), name='schema-swagger-ui'),
    re_path(
        r'^redoc/$', schema_view.with_ui('redoc', cache_timeout=0), name='schema-redoc'),
    # rest_framework urls.
    path('', include('rest_framework.urls', namespace='rest_framework')),
    # apps urls.
    path(f"{API_V1}/auth/", include("api_auth.urls", namespace='api_auth')),
    path(f"{API_V1}/products/", include("products.urls"), name="products"),
    path(f"{API_V1}/shopping/", include("shopping.urls"), name="shopping"),
]
