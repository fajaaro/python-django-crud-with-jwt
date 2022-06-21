from django.http import JsonResponse

class Response:
    def __init__(self, success = True, error = None, data = None, message = None, status_code = 200):
        self.success = success
        self.error = error
        self.data = data
        self.message = message
        self.status_code = status_code

    def to_json(self):
        res = JsonResponse({
            'success': self.success,
            'error': self.error,
            'data': self.data,
            'message': self.message,
        })
        res.status_code = self.status_code

        return res

    