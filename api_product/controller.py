from api_product.repository import ProductRepository
from intro.helpers.main_helper import MainHelper
from intro.models.response import Response
from slugify import slugify
import json

repo = ProductRepository()

class ProductController:
    def index(self, request):
        products = repo.get_all_product(order='desc')
        
        return Response(
            data=MainHelper.serialize_objects(products), 
            message='Success get all product.'
        ).to_json()

    def show(self, request, param_1):
        slug = param_1
        res = Response()

        product = None
        try:
            product = repo.get_product_by_slug(slug)
            if product is not None:
                res.data = product.to_json()
                res.message = "Product found."
            else:
                res.success = False
                res.error = "Product not found"
                res.status_code = 404
                return res.to_json()
        except Exception as e:
            res.success = False
            res.error = e.__class__.__name__ + ': ' + str(e)
            res.status_code = 500
            return res.to_json()

        return res.to_json()

    def store(self, request):
        payload = json.loads(request.body)
        res = Response()

        product = repo.get_product_by_slug(slugify(payload['name']))
        if product is not None:
            res.success = False
            res.error = "Name is used."
            res.status_code = 400
            return res.to_json()

        try:
            product = repo.create_product(payload)
            res.data = product.to_json()
            res.message = 'Product created.'
            res.status_code = 201
        except Exception as e:
            res.success = False
            res.error = e.__class__.__name__ + ': ' + str(e)
            res.status_code = 500
            return res.to_json()

        return res.to_json()

    def update(self, request, param_1):
        product_id = param_1
        payload = json.loads(request.body)
        res = Response()

        product = repo.get_product_by_id(product_id)
        if product is None:
            res.success = False
            res.error = "Product not found"
            res.status_code = 404
            return res.to_json()

        product.name = payload['name']
        product.slug = slugify(payload['name'])
        product.price = payload['price']
        repo.update(product)

        res.data = product.to_json()
        res.message = 'Product updated.'

        return res.to_json()