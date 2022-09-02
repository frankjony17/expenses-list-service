from rest_framework import routers

from shopping.views.shopping import ShoppingModelViewSet

app_name = "shopping"

router = routers.DefaultRouter(trailing_slash=False)
# products
router.register(r'', ShoppingModelViewSet, basename="shopping")

urlpatterns = router.urls
