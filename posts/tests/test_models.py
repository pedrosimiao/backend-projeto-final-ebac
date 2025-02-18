from django.test import TestCase

from posts.factories import PostFactory

class PostModelTest(TestCase):
    def test_post_and_retweet(self):
        original_post = PostFactory(content="Cool post to be retweeted")

        retweet = PostFactory(retweet=original_post, content="")

        self.assertIsNotNone(original_post.pk)
        self.assertIsNotNone(retweet.retweet )
        self.assertEqual(retweet.retweet.id, original_post.id)