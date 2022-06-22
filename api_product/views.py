from api_product.controller import ProductController
from django.views.decorators.http import require_http_methods
from intro.middleware.admin_middleware import admin
from intro.middleware.jwt_middleware import json_web_token

controller = ProductController()

@require_http_methods(['GET', 'POST'])
@json_web_token
@admin
def index_or_store(request, user):
    if request.method == 'GET':
        return controller.index(request, user)
    else:
        return controller.store(request, user)

@require_http_methods(['GET', 'PUT'])
@json_web_token
@admin
def show_or_update(request, user, param_1):
    if request.method == 'GET':
        return controller.show(request, user, param_1)
    else:
        return controller.update(request, user, param_1)