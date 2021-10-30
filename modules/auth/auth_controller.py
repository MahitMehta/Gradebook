from flask import Blueprint
from modules.auth.auth_service import AuthService
from utils.request_tools import body

auth = Blueprint('auth', __name__)
auth_service = AuthService()

@auth.route('/auth/login', methods=['POST'])
@body
def login(body): 
    userId, password = (body['userId'], body['pass'])
    return auth_service.login(userId, password)