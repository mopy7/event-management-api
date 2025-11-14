from django.urls import path, include
from .views import RegisterView, LoginView, EventViewSet
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register("", EventViewSet, basename="events")

urlpatterns = [
  path('register/', RegisterView.as_view(), name='register'),
  path('login/', LoginView.as_view(), name='login'),
  path("", include(router.urls)),
]