import factory

from django.utils import timezone

from posts.models.post import Post

from accounts.factories import UserFactory


class PostFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = Post

    user = factory.SubFactory(UserFactory)
    content = factory.Faker("text", max_nb_chars=280)

    created_at = factory.LazyFunction(lambda: timezone.now())


# Exemplo de uso:
# post = PostFactory()
# Cria um post com um usuário gerado automaticamente e conteúdo aleatório.
