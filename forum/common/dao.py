from model import Board, User

from common import db


# User
def select_user(username: str) -> User | None:
    query = "SELECT username, email, website FROM User WHERE username = ?"
    rows = db.query_database(query, (username,))
    return User.from_dict(rows[0]) if rows else None


def select_user_with_pw(username: str) -> User | None:
    query = "SELECT username, password, email, website FROM User WHERE username = ?"
    rows = db.query_database(query, (username,))
    return User.from_dict(rows[0]) if rows else None


# Board
def select_board(name: str) -> Board | None:
    query = "SELECT name, full_name, description FROM Board WHERE name = ?"
    rows = db.query_database(query, (name,))
    return Board.from_dict(rows[0]) if rows else None
