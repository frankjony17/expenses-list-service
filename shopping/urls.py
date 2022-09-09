from rest_framework import routers

from shopping.views.purchases import PurchasesModelViewSet
from shopping.views.shopping import ShoppingModelViewSet

app_name = "shopping"

router = routers.DefaultRouter(trailing_slash=False)
# products
router.register(r'shopping', ShoppingModelViewSet, basename="shopping")
router.register(r'purchases', PurchasesModelViewSet, basename="purchases")

urlpatterns = router.urls
