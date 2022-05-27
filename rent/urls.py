from rest_framework.routers import DefaultRouter
from .views import RentViewSet,RentedViewSet

router = DefaultRouter()
router.register("rent",RentViewSet)
router.register("rented",RentedViewSet)
urlpatterns = router.urls