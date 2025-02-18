from django.db import models
from django.conf import settings

class Post(models.Model):
    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    content = models.TextField()
    url = models.URLField(blank=True, null=True)
    image = models.ImageField(upload_to="posts/images/", blank=True, null=True)
    video = models.FileField(upload_to="posts/videos/", blank=True, null=True)
    created_at = models.DateField(auto_now_add=True)

    retweet = models.ForeignKey(
        'self',
        null=True,
        blank=True,
        on_delete=models.SET_NULL,
        related_name='retweets'
    )

    def __str__(self):
        if self.retweet:
            return f"{self.user.username} retweeted: {self.retweet.content[:30]}"
        return f"{self.user.username}: {self.content[:30]}"