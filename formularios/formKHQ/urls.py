from . import views
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', views.FormKHQViewSet, basename='formKHQ')
urlpatterns = router.urls