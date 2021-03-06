from flask import Blueprint, abort, flash, redirect, render_template, request
from flask_login import current_user

import utils
from common import dao

views = Blueprint("views", __name__)


@views.route("/", methods=["GET"])
@views.route("/boards", methods=["GET"])
def boards() -> str:
    boards = dao.select_all_boards()
    return render_template("boards.html", boards=boards, user=current_user)


@views.route("/boards/<string:name>", methods=["GET"])
@views.route("/boards/<string:name>/posts", methods=["GET"])
def board(name: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)
    posts = dao.select_posts(board.name, 100)
    return render_template("board.html", board=board, posts=posts, user=current_user)


@views.route("/boards/<string:name>/posts/<string:hex_id>", methods=["GET"])
def post(name: str, hex_id: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)

    try:
        id = int(hex_id, base=16)
    except ValueError:
        return abort(404)

    post = dao.select_post(id)
    utils.abort_if_falsy(post, 404)

    # Example:
    #   Post with ID=1 was posted in /prog/ and I want to access it
    #   using /boards/prog/posts/0x1 without this check it would be
    #   accessibile using /boards/<any-valid-board-name>/posts/0x1
    utils.abort_if_falsy(post.board == board.name, 404)

    comments = dao.select_comments(post.id)

    return render_template(
        "post.html", board=board, post=post, user=current_user
    )  # comments=comments


@views.route("/boards/<string:name>/new", methods=["GET", "POST"])
def new_post(name: str) -> str:
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)

    # Only authenticated users can see the form to create new posts
    # and call the endpoint to submit them.
    if not current_user.is_authenticated:
        return redirect(f"/boards/{board}")  # Redirect or a simple 403?

    if request.method == "POST":
        creator = current_user.username
        title = str(request.form.get("title")).strip()
        body = str(request.form.get("body")).strip()
        is_link = str(request.form.get("is_link")) == "on"

        if is_link and not utils.is_url_valid(body):
            flash("Invalid link")
        else:
            # Note that is the inputs contain HTML tags that's OK.
            # They are escaped automatically by Jinja.
            if title == "" or body == "":
                flash("No empty fields allowed")
            else:
                try:
                    post = dao.insert_post(name, creator, title, body, is_link)
                except:  # TODO: specify exception type
                    return abort(500)

                return redirect(f"/boards/{name}/posts/{hex(post.id)}")

    return render_template("new.html", board=board, user=current_user)


@views.route("/boards/<string:name>/posts/<string:hex_id>/new", methods=["GET", "POST"])
def new_comment(name: str, hex_id: str) -> str:
    print("HERE")
    board = dao.select_board(name)
    utils.abort_if_falsy(board, 404)

    try:
        id = int(hex_id, base=16)
    except ValueError:
        return abort(404)

    post = dao.select_post(id)
    utils.abort_if_falsy(post, 404)

    # Only authenticated users can see the form to create new comments
    # and call the endpoint to submit them.
    if not current_user.is_authenticated:
        return redirect(f"/boards/{board}/posts/{hex_id}")  # Redirect or a simple 403?

    if request.method == "POST":
        creator = current_user.username
        body = str(request.form.get("body")).strip()

        try:
            comment = dao.insert_comment(post.id, creator, body, None)
        except Exception as e:  # TODO: specify exception type
            return abort(500)

        return redirect(f"/boards/{name}/posts/{hex(post.id)}")

    return render_template("comment.html", board=board, post=post)


@views.route("/users/<string:username>", methods=["GET"])
def user(username: str) -> str:
    user = dao.select_user(username)
    utils.abort_if_falsy(user, 404)
    return render_template("user.html", subject=user, user=current_user)
