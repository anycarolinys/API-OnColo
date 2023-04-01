from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.FormQVCViewSet, basename='formKHQ')
urlpatterns = router.urls