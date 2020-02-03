from flask_bootstrap import Bootstrap
from flask_sqlalchemy import SQLAlchemy
from flask_mail import Mail
from flask_login import LoginManager
from flask_moment import Moment

bootstrap = Bootstrap()
mail = Mail()
db = SQLAlchemy()
moment = Moment()

login_manager = LoginManager()
