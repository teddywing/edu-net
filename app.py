import os

from flask import Flask

from flask_user import SQLAlchemyAdapter, UserManager

from modules.shared.models import db
from modules.interest.models import Interest, UserInterest
from modules.user.models import User, UserAuth

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///development.db'
app.config['SECRET_KEY'] = 'this should definitely be changed to an ' \
    'environment variable'
if not os.environ.get('EDU_APP_ENV'):
    app.debug = True
db.init_app(app)

with app.app_context():
    db.create_all()

# Setup Flask-User
db_adapter = SQLAlchemyAdapter(db,  User, UserAuthClass=UserAuth)
user_manager = UserManager(db_adapter, app)

@app.route("/")
def hello():
    return "Hello World!"

if __name__ == "__main__":
    app.run()
