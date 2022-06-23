from intro.repositories.repository import Repository
from authentication.models import User
from passlib.hash import sha256_crypt

class UserRepository(Repository):
    def get_all_user(self, order='desc'):
        order_symbol = '-' if order == "desc" else ''
        return User.objects.all().order_by(order_symbol + 'id')

    def get_user_by_email(self, email):
        return User.objects.filter(email=email).first()

    def get_user_by_id(self, id):
        return User.objects.filter(id=id).first()

    def create_user(self, payload):
        user = User.objects.create(
            name=payload['name'], 
            email=payload['email'], 
            password=sha256_crypt.encrypt(payload['password'])
        )
        user.save()

        return user