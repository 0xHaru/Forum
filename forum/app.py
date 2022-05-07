from flask import Flask

from views import views


def create_app(config_filename: str = "config.py") -> Flask:
    app = Flask(__name__)
    app.config.from_pyfile(config_filename)

    app.register_blueprint(views, url_prefix="/")
    # app.register_blueprint(auth, url_prefix="/")

    return app


if __name__ == "__main__":
    app = create_app()
    app.run(host="0.0.0.0", port=8000, debug=True)
