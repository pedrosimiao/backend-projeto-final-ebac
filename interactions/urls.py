from django.urls import path, include
from rest_framework.routers import DefaultRouter
from interactions.viewsets.like_viewset import LikeViewSet
from interactions.viewsets.comment_viewset import CommentViewSet

router = DefaultRouter()
router.register(r"likes", LikeViewSet, basename="likes")
router.register(r"comments", CommentViewSet, basename="comments")

urlpatterns = [
    path("", include(router.urls)),
]
