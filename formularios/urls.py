from django.urls import path
from .views import FormulariosView

urlpatterns = [
    path('', FormulariosView.as_view(), name='formsview'),
]