from rest_framework.routers import DefaultRouter
from .views import FormAGPGViewSet

router = DefaultRouter()
router.register(r'', FormAGPGViewSet, basename='FormAGPG')
urlpatterns = router.urls