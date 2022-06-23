from intro.middleware.admin_middleware import admin
from intro.middleware.jwt_middleware import json_web_token
from user.controller import UserController
from django.views.decorators.http import require_http_methods

controller = UserController()

@require_http_methods(['GET'])
@json_web_token
@admin
def index(request, user):
    return controller.index()
    
@require_http_methods(['GET', 'PUT', 'DELETE'])
@json_web_token
@admin
def show_or_update_or_delete(request, user, user_id):
    if request.method == 'GET':
        return controller.show(user_id)
    elif request.method == 'PUT':
        return controller.update(request, user_id)
    else:
        return controller.delete(user_id)
