from flask import Flask
from flask_login import LoginManager

from common import dao
from model import User


def create_app(config_filename: str = "config.py") -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    from auth import auth

    login_manager = LoginManager()
    login_manager.login_view = "/login"
    login_manager.init_app(app)

    @login_manager.user_loader  # type: ignore
    def load_user(username: str) -> User | None:
        return dao.select_user(username)

    from views import views

    app.register_blueprint(views, url_prefix="/")
    app.register_blueprint(auth, url_prefix="/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
