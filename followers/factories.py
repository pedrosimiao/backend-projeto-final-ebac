# followers/factories.py
import factory
from followers.models.follower import Follower
from accounts.factories import UserFactory


class FollowerFactory(factory.django.DjangoModelFactory):
    class Meta:
        model = Follower

    following = factory.SubFactory(UserFactory)
    follower = factory.SubFactory(UserFactory)
    created_at = factory.Faker("date_time_this_year")


# Exemplo de uso:
# follow = FollowerFactory()
