from rest_framework import viewsets, permissions
from interactions.models.like import Like
from interactions.serializers.like_serializer import LikeSerializer

class LikeViewSet(viewsets.ModelViewSet):
    queryset = Like.objects.all().order_by("-created_at")
    serializer_class = LikeSerializer
    permission_classes = [permissions.IsAuthenticated]