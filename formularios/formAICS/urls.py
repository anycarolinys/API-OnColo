from rest_framework.routers import DefaultRouter
from .views import FormAICSViewSet

router = DefaultRouter()
router.register(r'', FormAICSViewSet, basename='FormAICS')
urlpatterns = router.urls