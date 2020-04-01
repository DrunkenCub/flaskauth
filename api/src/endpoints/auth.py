from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ..models import User
from ..api import db

auth_bp = Blueprint('auth', __name__, url_prefix='/auth')

class RegisterAPI(MethodView):
    def post(self):
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')
        first_name = post_data.get('first_name')
        try:
            user = User.query.filter_by(email='email').first()
            if user:
                responseObject = {
                    'message': 'User already exists!'
                }
                return make_response(jsonify(responseObject)), 400
            else:
                user = User(
                    email = email,
                    first_name = first_name
                )
                user.set_password(password)

                try:
                    db.session.add(user)
                    db.session.commit()

                except Exception as e:
                    raise e

                responseObject = {
                    'message': 'user created',
                    'result': user.to_json()
                }
                # used 201 as opposed to 200 since its a user creation
                return make_response(jsonify(responseObject)), 201  
        except Exception as e:
            raise e    

    def get(self):
        pass

    def put(self):
        pass


class LoginAPI(MethodView):
    def post(self):
        post_data = request.get_json()
        email = post_data.get('email')
        password = post_data.get('password')

        try:
            user = User.query.filter_by(email=email).first()
            if user is None:
                responseObject = {
                    'message': 'User does not exist!'
                }
                return make_response(jsonify(responseObject)), 400
            else:
                responseObject = {
                    'message': 'Successfully logged in',
                    'user': user.to_json(),
                    'auth_token': user.encode_auth_token(user.id).decode()
                }
                return make_response(jsonify(responseObject)), 200
        except Exception as e:
            raise e
    def get(self):
        pass



registration_view = RegisterAPI.as_view('register_api')
login_view = LoginAPI.as_view('login_api')


auth_bp.add_url_rule('/signup', view_func=registration_view, methods=['POST'])
auth_bp.add_url_rule('/login', view_func=login_view, methods=['POST'])
