import json
from authentication.repository import UserRepository
from intro.models.response import Response
from intro.helpers.main_helper import MainHelper

repo = UserRepository()

class UserController:
    def index(self):
        users = repo.get_all_user()

        return Response(
            data=MainHelper.serialize_objects(users),
            message='Success get all user.'
        ).to_json()

    def show(self, user_id):
        res = Response()

        user = None
        try:
            user = repo.get_user_by_id(user_id)
            if user is not None:
                res.data = user.to_json()
                res.message = "User found."
            else:
                res.success = False
                res.error = "User not found"
                res.status_code = 404
                return res.to_json()
        except Exception as e:
            res.success = False
            res.error = e.__class__.__name__ + ': ' + str(e)
            res.status_code = 500
            return res.to_json()

        return res.to_json()

    def update(self, request, user_id):
        payload = json.loads(request.body)
        res = Response()

        user = repo.get_user_by_id(user_id)
        if user is None:
            res.success = False
            res.error = "User not found."
            res.status_code = 404
            return res.to_json()

        existing_user = repo.get_user_by_email(payload['email'])
        if existing_user is not None and existing_user != user:
            res.success = False
            res.error = "Email used. Please use another email."
            res.status_code = 400
            return res.to_json()

        user.name = payload['name']
        user.role = payload['role']
        user.email = payload['email']
        repo.update(user)

        res.data = user.to_json()
        res.message = "User updated."
        return res.to_json()

    def delete(self, user_id):
        res = Response()

        user = repo.get_user_by_id(user_id)
        if user is None:
            res.success = False
            res.error = "User not found."
            res.status_code = 404
            return res.to_json()

        repo.delete(user)

        res.message = "User deleted."
        return res.to_json()

