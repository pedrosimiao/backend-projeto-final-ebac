from rest_framework import viewsets, permissions
from followers.models.follower import Follower
from followers.serializers.follower_serializer import FollowerSerializer


class FollowerViewSet(viewsets.ModelViewSet):
    queryset = Follower.objects.all().order_by("-created_at")
    serializer_class = FollowerSerializer
    permission_classes = [permissions.IsAuthenticated]
