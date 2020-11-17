# coding=utf-8
# services/main/project/__init__.py

import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
# from flask_debugtoolbar import DebugToolbarExtension

# instantiate the db
db = SQLAlchemy()
# toolbar = DebugToolbarExtension()


def create_app(script_info=None):

    # instanciado la  app
    app = Flask(__name__)
    # set config
    app_settings = os.getenv('APP_SETTINGS')
    app.config.from_object(app_settings)

    # configurar la extension
    db.init_app(app)
    # toolbar.init_app(app)  # nuevo

    # registrar blueprints
    from project.api.usuarios import usuarios_blueprint
    from project.api.encuesta import encuesta_blueprint

    app.register_blueprint(usuarios_blueprint)
    app.register_blueprint(encuesta_blueprint)

    # contexto shell para flask cli
    @app.shell_context_processor
    def ctx():
        return {'app': app, 'db': db}

    return app

# instanciando la app
# app = Flask(__name__)

# api = Api(app)

# establecer configuración
# app.config.from_object("project.config.DevelopmentConfig")  # nuevo

# estableciendo config
