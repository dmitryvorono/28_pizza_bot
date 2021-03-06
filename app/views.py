from app.flask_server import app
from functools import wraps
from flask import request, Response, render_template
from config import admin_name, admin_password
from http import HTTPStatus


def check_auth(username, password):
    """This function is called to check if a username /
    password combination is valid.
    """
    return username == admin_name and password == admin_password


def authenticate():
    return Response('Could not verify your access level for that URL.\n'
                    'You have to login with proper credentials',
                    HTTPStatus.UNAUTHORIZED,
                    {'WWW-Authenticate': 'Basic realm="Login Required"'})


def requires_auth(function):
    @wraps(function)
    def decorated(*args, **kwargs):
        auth = request.authorization
        if not auth or not check_auth(auth.username, auth.password):
            return authenticate()
        return function(*args, **kwargs)
    return decorated


@app.route('/admin/')
@requires_auth
def secret_page():
    return render_template('admin/index.html')
