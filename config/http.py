from flask import Flask
from flask_cors import CORS
from helpers import sql_alchemy, jwt_manager
from flask_mail import Mail
from flask_migrate import Migrate
from models import user
import routes

cors = CORS()
mail = Mail()

def create_app(configuration):
    app = Flask(
        __name__.split(',')[0],
        static_url_path='/static',
        static_folder='../static'
    )

    app.config['JSON_SORT_KEYS'] = False
    app.config["JWT_SECRET_KEY"] = configuration.JWT_SECRET

    # load configuration
    app.config.from_object(configuration)

    # register route blueprint
    app.register_blueprint(routes.session.blueprint, url_prefix='/api/v1/user')
    app.register_blueprint(routes.user.blueprint, url_prefix='/api/v1/user')
    ##

    # init app
    cors.init_app(app, resources={r"/*": {"origins": "*"}})
    sql_alchemy.init_app(app)
    mail.init_app(app)
    migrate = Migrate(app, sql_alchemy)
    jwt_manager.init_app(app)

    return app
