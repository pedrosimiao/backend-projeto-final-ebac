from rest_framework import serializers
from followers.models.follower import Follower


class FollowerSerializer(serializers.ModelSerializer):
    class Meta:
        model = Follower
        fields = ["id", "following", "follower", "created_at"]
