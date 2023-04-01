from django.urls import path, include
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView
from autenticacao.views import LoginViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register(r'', LoginViewSet, basename='login')
urlpatterns = router.urls
