import factory

from django.utils import timezone

from interactions.models.like import Like
from interactions.models.comment import Comment

from posts.factories import PostFactory
from accounts.factories import UserFactory


class LikeFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Like

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)
    created_at = factory.LazyFunction(lambda: timezone.now())


class CommentFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Comment

    user = factory.SubFactory(UserFactory)
    post = factory.SubFactory(PostFactory)

    content = factory.Faker("sentence")

    created_at = factory.LazyFunction(lambda: timezone.now())


# Exemplo de uso:
# like = LikeFactory()
# comment = CommentFactory()
