from . import views
from rest_framework.routers import DefaultRouter


router = DefaultRouter()
router.register(r'', views.FormAPRViewSet, basename='formAPR')
urlpatterns = router.urls
