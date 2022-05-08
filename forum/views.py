from flask import Blueprint, render_template

import utils
from common import dao

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
@views.route("/boards", methods=["GET"])
def boards() -> str:
    boards = dao.select_all_boards()
    return render_template("boards.html", boards=boards)


@views.route("/boards/<string:name>", methods=["GET"])
def board(name: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)
    posts = dao.select_posts(board.name, 100)
    return render_template("board.html", board=board, posts=posts)


@views.route("/boards/<string:name>/posts/<string:id>", methods=["GET"])
def post(name: str, id: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)

    post = dao.select_post(int(id, base=16))
    utils.abort_if_falsy(post, 404)

    return render_template("post.html", post=post)


@views.route("/users/<string:username>", methods=["GET"])
def user(username: str) -> str:
    user = dao.select_user(username)
    utils.abort_if_falsy(user, 404)
    return render_template("user.html", user=user)
