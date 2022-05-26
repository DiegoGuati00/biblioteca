from rest_framework.routers import DefaultRouter
from .views import AutorViewSet, BookItemViewSet, BookViewSet

router = DefaultRouter()
router.register("autor",AutorViewSet)
router.register("book",BookViewSet)
router.register("bookitem",BookItemViewSet)
urlpatterns = router.urls