from flask import Flask

def create_app():
    app = Flask(__name__)
    app.config['SECRET_KEY'] = 'secret here'


    from .views import views
    from .auth import auth

    #register blueprints with flask application
    app.register_blueprint(views, url_prefix= "/")  #/ mwans no prefix in url
    app.register_blueprint(auth, url_prefix="/")

    return app