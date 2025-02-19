from rest_framework import serializers
from posts.models.post import Post


class PostSerializer(serializers.ModelSerializer):
    user = serializers.PrimaryKeyRelatedField(read_only=True)
    # Permite que 'content' seja vazio
    content = serializers.CharField(required=False, allow_blank=True)
    retweet = serializers.SerializerMethodField()
    retweet_id = serializers.IntegerField(
        write_only=True, required=False, allow_null=True
    )

    class Meta:
        model = Post
        fields = [
            "id",
            "user",
            "content",
            "url",
            "image",
            "video",
            "created_at",
            "retweet",
            "retweet_id",
        ]

    def get_retweet(self, obj):
        if obj.retweet:
            return {
                "id": obj.retweet.id,
                "user": obj.retweet.user.username,
                "content": obj.retweet.content,
                "created_at": obj.retweet.created_at.isoformat(),
            }
        return None

    def create(self, validated_data):
        retweet_id = validated_data.pop("retweet_id", None)
        if retweet_id:
            validated_data["retweet"] = Post.objects.get(id=retweet_id)
        return super().create(validated_data)
