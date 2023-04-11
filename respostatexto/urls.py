from rest_framework.routers import DefaultRouter
from views import RespostaTextoViewSet

router = DefaultRouter()
router.register(r'', RespostaTextoViewSet, basename='RespostaTexto')
urlpatterns = router.urls