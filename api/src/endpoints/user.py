from flask import Blueprint, request, make_response, jsonify
from flask.views import MethodView
from ..models import User
from ..api import db
from ..helpers.auth_helper import login_required



user_bp = Blueprint('user', __name__, url_prefix='/users')


class UserAPI(MethodView):
    def post(self):
        pass

    @login_required
    def get(self, user_id):
        try:
            if user_id is not None:
                user = User.query.filter_by(id=user_id).first()
            else:
                user = User.query.all()
            
            responseObject = {
                'message': 'Resoruce fetched',
                'users': [u.to_json() for u in user]

            }
            return make_response(jsonify(responseObject)), 200
        except Exception as e:
            raise e

    def put(self):
        pass



user_view = UserAPI.as_view('user_api')


user_bp.add_url_rule('/<user_id>', view_func=user_view, methods=['GET'])
user_bp.add_url_rule('', defaults={'user_id': None}, view_func=user_view, methods=['GET'])
