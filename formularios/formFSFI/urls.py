from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.FormFSFIViewSet, basename='formFSFI')
urlpatterns = router.urls
