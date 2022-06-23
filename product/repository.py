from intro.repositories.repository import Repository
from product.models import Product
from slugify import slugify

class ProductRepository(Repository):
    def get_all_product(self, order='desc'):
        order_symbol = '-' if order == "desc" else ''
        return Product.objects.all().order_by(order_symbol + 'id')

    def get_products_by_user(self, user):
        return user.product_set.all()

    def get_product_by_id(self, id):
        return Product.objects.filter(id=id).first()

    def get_product_by_slug(self, slug):
        return Product.objects.filter(slug=slug).first()

    def create_product(self, payload):
        product = Product.objects.create(
            author_id=payload['author_id'],
            name=payload['name'], 
            slug=slugify(payload['name']), 
            price=payload['price']
        )
        product.save()

        return product