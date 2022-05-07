from flask import Blueprint, Response, flash, redirect, render_template, request
from flask_login import login_user
from werkzeug.security import check_password_hash

from common import dao

auth = Blueprint("auth", __name__)


@auth.route("/login", methods=["GET", "POST"])
def login() -> str | Response:
    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.select_user_with_pw(username)

        if user:
            if not check_password_hash(user.password, password):  # type: ignore
                flash("Incorrect password.")
            else:
                login_user(user, remember=True)
                return redirect("/")
        else:
            flash("Username does not exist.")

    return render_template("login.html")
