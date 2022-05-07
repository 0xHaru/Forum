from models import Board, User

from common import db


# User
def select_user(username: str) -> User | None:
    query = "SELECT username, email, website FROM User WHERE username = ?"
    rows = db.query_database(query, (username,))
    return None if not rows else User.from_dict(rows[0])


def select_user_with_pw(username: str) -> User | None:
    query = "SELECT username, password, email, website FROM User WHERE username = ?"
    rows = db.query_database(query, (username,))
    return None if not rows else User.from_dict(rows[0])


# Board
def select_board(name: str) -> Board | None:
    query = "SELECT name, full_name, description FROM Board WHERE name = ?"
    rows = db.query_database(query, (name,))
    return None if not rows else Board.from_dict(rows[0])


def select_all_boards() -> list[Board]:
    query = "SELECT name, full_name, description FROM Board"
    rows = db.query_database(query)
    return [] if not rows else [Board.from_dict(row) for row in rows]
