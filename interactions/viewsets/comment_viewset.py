from rest_framework import viewsets, permissions
from interactions.models.comment import Comment
from interactions.serializers.comment_serializer import CommentSerializer

class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by("-created_at")
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticated]