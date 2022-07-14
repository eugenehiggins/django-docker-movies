from django.urls import path
from rest_framework import routers

from movies.views import MovieViewSet

router = routers.DefaultRouter()

router.register(r"api/movies", MovieViewSet)

urlpatterns = router.urls
