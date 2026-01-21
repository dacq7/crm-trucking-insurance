from flask import Flask
from crm_app.extensions import db, migrate


def build_app():
    app = Flask(__name__)

    app.config.from_object("crm_app.config.Config")

    db.init_app(app)
    migrate.init_app(app, db)

    from crm_app.routes.users import users_bp
    app.register_blueprint(users_bp)

    return app
