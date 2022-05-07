from flask import Blueprint, abort  # , render_template

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
def index() -> str:
    return "index"
    # return render_template("index.html")


@views.route("/boards/<string:name>", methods=["GET"])
def board(name: str) -> str:
    if name not in ["prog", "tech", "math", "misc"]:
        abort(404)

    return "board"
    # return render_template("board.html", board=, posts=)


@views.route("/prog/<string:id>", methods=["GET"])
@views.route("/tech/<string:id>", methods=["GET"])
@views.route("/math/<string:id>", methods=["GET"])
@views.route("/misc/<string:id>", methods=["GET"])
def post(id: str) -> str:
    return "post"
    # return render_template("post.html")
