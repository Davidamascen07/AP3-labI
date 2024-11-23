from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config.from_object('config.Config')
    

    # Registro do Blueprint
    from app.routes import app_routes
    app.register_blueprint(app_routes, url_prefix='/')


    return app
