from django.urls import path, include
from rest_framework.routers import DefaultRouter
from posts.viewsets.post_viewset import PostViewSet

router = DefaultRouter()
router.register(r"posts", PostViewSet, basename="posts")

urlpatterns = [
    path("", include(router.urls)),
]
