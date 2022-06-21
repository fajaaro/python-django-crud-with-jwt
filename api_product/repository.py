from intro.repositories.repository import Repository
from api_product.models import Product
from slugify import slugify

class ProductRepository(Repository):
    def get_all_product(self, order='desc'):
        order_symbol = '-' if order == "desc" else ''
        return Product.objects.all().order_by(order_symbol + 'id')

    def get_product_by_id(self, id):
        return Product.objects.filter(id=id).first()

    def get_product_by_slug(self, slug):
        return Product.objects.filter(slug=slug).first()

    def create_product(self, payload):
        product = Product.objects.create(
            name=payload['name'], 
            slug=slugify(payload['name']), 
            price=payload['price']
        )
        product.save()

        return product