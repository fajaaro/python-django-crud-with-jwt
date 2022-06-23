from authentication.controller import AuthController
from django.views.decorators.http import require_http_methods

controller = AuthController()

@require_http_methods(['POST'])
def register(request):
    return controller.register(request)

@require_http_methods(['POST'])
def login(request):
    return controller.login(request)

@require_http_methods(['POST'])
def refresh_token(request):
    return controller.refresh_token(request)
