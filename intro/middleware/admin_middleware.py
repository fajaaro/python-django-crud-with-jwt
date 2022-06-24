from functools import wraps
from intro.models.response import Response 

def admin(f):
    @wraps(f)
    def decorator(request, user, *args, **kwargs):
        res = Response(success=True)
        
        if user.role != 'admin':
            res.success = False
            res.error = "Unauthorized. Need admin access."
            res.status_code = 403
            return res.to_json()

        return f(request, user, *args, **kwargs)
    return decorator
