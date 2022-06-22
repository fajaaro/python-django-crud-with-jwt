from datetime import datetime, timedelta
from api_auth.repository import UserRepository
from intro.models.response import Response
from passlib.hash import sha256_crypt
from django.conf import settings
import json
import jwt

repo = UserRepository()
SECRET_KEY = settings.SECRET_KEY

def generate_token(user):

    now = datetime.utcnow()
    access_token = jwt.encode({
        'user_id': user.id, 
        'exp': now + timedelta(minutes=30)
    }, SECRET_KEY, 'HS256')
    refresh_token = jwt.encode({
        'user_id': user.id, 
        'exp': now + timedelta(days=30)
    }, SECRET_KEY, 'HS256')
    
    return access_token, refresh_token

class AuthController:
    def register(self, request):
        payload = json.loads(request.body)
        res = Response()
        
        user = repo.get_user_by_email(payload['email'])
        if user is not None:
            res.success = False
            res.error = 'Email is registered.'
            res.status_code = 400
            return res.to_json()

        try:
            user = repo.create_user(payload)
            res.data = user.to_json()
            res.message = 'Register success.'
            res.status_code = 201
        except Exception as e:
            res.success = False
            res.error = e.__class__.__name__ + ': ' + str(e)
            res.status_code = 500
            return res.to_json()

        return res.to_json()

    def login(self, request):
        payload = json.loads(request.body)
        res = Response()

        user = repo.get_user_by_email(payload['email'])
        if user is None:
            res.success = False
            res.error = 'Email is not registered.'
            res.status_code = 400
            return res.to_json()

        verified = sha256_crypt.verify(payload['password'], user.password)

        if verified is True:
            user.last_login = datetime.now()
            repo.update(user)

            access_token, refresh_token = generate_token(user)

            res.data = {
                'user': user.to_json(),
                'token': {
                    'access_token': access_token,
                    'refresh_token': refresh_token
                }
            }
            res.message = 'Login success.'
            return res.to_json()
        else:
            res.success = False
            res.error = 'Wrong password.'
            res.status_code = 400
            return res.to_json()

    def refresh_token(self, request):
        payload = json.loads(request.body)
        res = Response()
        
        refresh_token = payload['refresh_token']

        try:
            data = jwt.decode(refresh_token, SECRET_KEY, algorithms=['HS256'])
        except Exception as e:
            res.success = False
            res.error = 'Refresh Token is invalid.'
            res.status_code = 401
            return res.to_json()

        user = repo.get_user_by_id(data['user_id'])
        if user is None:
            res.success = False
            res.error = 'Refresh Token is invalid.'
            res.status_code = 401
            return res.to_json()
        
        access_token, _ = generate_token(user)

        res.data = {'access_token': access_token}
        res.message = 'Access token has been updated.'
        return res.to_json()