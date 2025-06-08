import factory

from django.contrib.auth.models import User
from product.factories import ProductFactory

from order.models import Order
from pydantic.v1.errors import cls_kwargs

class UserFactory (factory.django.DjandoModelFactory):
    email = factory.Faker('pystr')
    username = factory.Faker('pystr')

    class Meta:
        model = User

class OrderFactory(factory.django.DjandoModelFactory):
    user = factory.SubFactory(UserFactory)

    @factory.post_generation
    def product(self, create, extrate, **kwargs):
        if not create:
            return

        if extrate:
            for product in extrate:
                self.product.add(product)

                class Meta:
                    model = Order



