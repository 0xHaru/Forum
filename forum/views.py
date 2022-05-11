from flask import Blueprint, render_template
from flask_login import current_user

import utils
from common import dao

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
@views.route("/boards", methods=["GET"])
def boards() -> str:
    boards = dao.select_all_boards()
    return render_template("boards.html", 
        boards=boards, user=current_user)


@views.route("/boards/<string:name>", methods=["GET"])
@views.route("/boards/<string:name>/posts", methods=["GET"])
def board(name: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)
    posts = dao.select_posts(board.name, 100)
    return render_template("board.html", 
        board=board, posts=posts, user=current_user)


@views.route("/boards/<string:name>/posts/<string:id>", methods=["GET"])
def post(name: str, id: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)

    # TODO: int() throws ValueError if <id> is an invalid literal
    post = dao.select_post(int(id, base=16))
    utils.abort_if_falsy(post, 404)

    # Example:
    #   Post with ID=1 was posted in /prog/ and I want to access it
    #   using /boards/prog/posts/0x1 without this check it would be
    #   accessibile using /boards/<any-valid-board-name>/posts/0x1
    utils.abort_if_falsy(post.board == board.name, 404)

    return render_template("post.html", 
        post=post, user=current_user)


@views.route("/users/<string:username>", methods=["GET"])
def user(username: str) -> str:
    user = dao.select_user(username)
    utils.abort_if_falsy(user, 404)
    return render_template("user.html", subject=user, user=current_user)
