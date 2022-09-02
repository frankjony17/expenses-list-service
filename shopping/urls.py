from rest_framework import routers

from shopping.views.shopping import ShoppingModelViewSet

router = routers.DefaultRouter()
# products
router.register(r'', ShoppingModelViewSet, basename="shopping")

urlpatterns = [] + router.urls
