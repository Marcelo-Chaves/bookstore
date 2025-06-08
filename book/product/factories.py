import factory
from factory import LazyAttribute

from product.models import Product
from product.models import Category

class CategoryFactory (factory.django.DjandoModelFactory):
    title = factory.Faker('pystr')
    slug= factory.Faker('pystr')
    description = factory.Faker('pystr')
    active = factory.Interator([True, False])

    class Meta:
        model = Category

class ProductFactory (factory.django.DjangoModelFactory):
    price = factory.Faker('pystr')
    category = LazyAttribute(CategoryFactory)
    title = factory.Faker('pystr')

    @factory.post_generation
    def category(self, create, extrate, **kwargs):
        if not create:
            return

        if extrate:
            for category in extrate:
                self.category.add(category)

                class Meta:
                    model = Product
