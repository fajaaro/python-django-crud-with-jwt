from intro.repositories.repository import Repository
from api_auth.models import User
from passlib.hash import sha256_crypt

class UserRepository(Repository):
    def get_user_by_email(self, email):
        return User.objects.filter(email=email).first()

    def create_user(self, payload):
        user = User.objects.create(
            name=payload['name'], 
            email=payload['email'], 
            password=sha256_crypt.encrypt(payload['password'])
        )
        user.save()

        return user