from flask import *
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import CSRFProtect
from flask_socketio import SocketIO, emit
from gevent.pywsgi import WSGIServer
from gevent import monkey
monkey.patch_all()
import os
from functools import wraps
app = Flask(__name__)
socketio = SocketIO(app)
csrf = CSRFProtect(app)
db = SQLAlchemy(app)

class role:
    def __init__(self, name, rolenum):
        self.name = name
        self.rolenum = rolenum
    def __lt__(self, other):
        return self.rolenum > other.rolenum
    def __le__(self, other):
        return self.rolenum >= other.rolenum
    def __eq__(self, other):
        return self.rolenum == other.rolenum
    def __repr__(self):
        return f"role({self.name}, {self.rolenum})"
    def __str__(self):
        return self.name

user = role("user", 0)
logged_user = role("logged_user", 1)
good_user = role("good_user", 2)
vip = role("vip", 3)
vvip = role("vvip", 4)
vvvip = role("vvvip", 5)
admin = role("admin", 6)
owner = role("owner", 7)
roles = {
    "user":user,
    "logged_user":logged_user,
    "good_user":good_user,
    "vip":vip,
    "vvip":vvip,
    "vvvip":vvvip,
    "admin":admin,
    "owner":owner
}
def role_required(required_role):
    def decorator(f):
        @wraps(f)
        def decorated_function(*args, **kwargs):
            if "role" not in session or roles[session[f'{required_role}']] < required_role:
                return "<h1 style=\"font-size:2rem; color:red;\">권한 부족</h1>", 403
            return f(*args, **kwargs)
        return decorated_function
    return decorator

@app.route('/')
def index():
    session['role'] = 'user'
    return render_template('index.html')

@app.route('/<path:filename>')
def serve_static(filename):
    return send_from_directory('static', filename)

if __name__ == '__main__':
    import ssl
    context = ssl.SSLContext(ssl.PROTOCOL_TLS_SERVER)
    context.load_cert_chain("key/fullchain.pem", "key/privkey.pem")
    socketio.run(app, host='0.0.0.0', port=443, ssl_context=context)
