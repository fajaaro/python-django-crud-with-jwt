from functools import wraps
from django.conf import settings
from authentication.repository import UserRepository
from intro.models.response import Response 
import jwt

SECRET_KEY = settings.SECRET_KEY
user_repository = UserRepository()

def json_web_token(f):
    @wraps(f)
    def decorator(request, *args, **kwargs):
        res = Response(success=True)
        authorization = request.headers['Authorization']

        token = None
        if authorization is not None:
            token = authorization.split()[1]

        if not token:
            res.success = False
            res.error = "A valid token is missing."
            res.status_code = 400
            return res.to_json()

        try:
            data = jwt.decode(token, SECRET_KEY, algorithms=["HS256"])
        except Exception as e:
            res.success = False
            res.error = "Token is invalid."
            res.status_code = 401
            return res.to_json()

        user = user_repository.get_user_by_id(data['user_id'])
        if user is None:
            res.success = False
            res.error = "Token is invalid."
            res.status_code = 401
            return res.to_json()

        return f(request, user, *args, **kwargs)
    return decorator
