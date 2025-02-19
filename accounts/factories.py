import factory
from django.contrib.auth import get_user_model

# Modelo de usuário personalizado definido em AUTH_USER_MODEL (accounts.User)
User = get_user_model()


class UserFactory(factory.django.DjangoModelFactory):

    class Meta:
        model = User

    username = factory.Faker("user_name")
    email = factory.Faker("email")
    password = factory.PostGenerationMethodCall("set_password", "123456")


# Exemplo de uso:
# user = UserFactory()
# Cria um usuário com username, email gerados aleatoriamente e senha "123456".
