from api_product.controller import ProductController
from django.views.decorators.http import require_http_methods

controller = ProductController()

@require_http_methods(['GET', 'POST'])
def index_or_store(request):
    if request.method == 'GET':
        return controller.index(request)
    else:
        return controller.store(request)

@require_http_methods(['GET', 'PUT'])
def show_or_update(request, param_1):
    if request.method == 'GET':
        return controller.show(request, param_1)
    else:
        return controller.update(request, param_1)