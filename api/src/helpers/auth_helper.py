from flask import request
from flask import abort
from functools import wraps

from ..models import User

def login_required(fn):
    @wraps(fn)
    def wrapper(*args, **kwargs):
        auth_header = request.headers.get('Authorization')
        
        if auth_header is None:
            abort(401)
        try:
            User.decode_auth_token(auth_header)
        except:
            abort(401)
        return fn(*args, **kwargs)
    return wrapper