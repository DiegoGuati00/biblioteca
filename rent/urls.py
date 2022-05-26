from rest_framework.routers import DefaultRouter
from .views import RentViewSet

router = DefaultRouter()
router.register("rent",RentViewSet)
urlpatterns = router.urls