from flask import (Blueprint, Response, flash, redirect, render_template,
                   request)
from flask_login import login_required, login_user, logout_user, current_user
from werkzeug.security import check_password_hash, generate_password_hash

from common import dao

auth = Blueprint("auth", __name__)

@auth.route("/signup", methods=["GET", "POST"])
def signup() -> str | Response:

    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")
        password2 = request.form.get("confirm-password")

        err = None
        if password != password2:
    
            err = "Password confirmation failed"
        else:

            hashed = generate_password_hash(password)
            user = dao.insert_user(username, hashed)

            if user is None:
                
                if dao.select_user(username) is not None:
                    err = "Username already in use"
                else:
                    err = "Unknown failure"
        
        if err is None:
            login_user(user, remember=True)
            return redirect("/")
        else:
            flash(err)

    return render_template("signup.html")


@auth.route("/login", methods=["GET", "POST"])
def login() -> str | Response:

    if current_user.is_authenticated:
        return redirect("/")

    if request.method == "POST":
        username = request.form.get("username")
        password = request.form.get("password")

        user = dao.select_user_with_pw(username)

        if user is not None:
            if not check_password_hash(user.password, password):  # type: ignore
                flash("Incorrect password.")
            else:
                login_user(user, remember=True)
                return redirect("/")
        else:
            flash("Username does not exist.")

    return render_template("login.html")


@auth.route("/logout", methods=["GET"])
@login_required  # type: ignore
def logout() -> Response:
    logout_user()
    return redirect("/")
