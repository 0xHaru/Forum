from datetime import datetime

from models import Board, Comment, Post, User

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


def insert_user(username: str, password: str) -> User | None:
    stmt = "INSERT INTO User(username, password) VALUES (?, ?)"
    try:
        db.modify_database(stmt, (username, password))
    except db.DBError as e:
        return None
    return User(username, password)


# Board
def select_board(name: str) -> Board | None:
    query = "SELECT name, full_name, description FROM Board WHERE name = ?"
    rows = db.query_database(query, (name,))
    return None if not rows else Board.from_dict(rows[0])


def select_all_boards() -> list[Board]:
    query = "SELECT name, full_name, description FROM Board"
    rows = db.query_database(query)
    return [] if not rows else [Board.from_dict(row) for row in rows]


# Post
def select_post(id: int) -> Post | None:
    query = "SELECT id, board, creator, title, body, is_link, timestamp FROM Post WHERE id = ?"
    rows = db.query_database(query, (id,))
    return None if not rows else Post.from_dict(rows[0])


# TODO: do not select the body if is_link = false
def select_posts(board: str, limit: int) -> list[Post]:
    query = """SELECT id, board, title, body, is_link, timestamp
               FROM Post
               WHERE board = ?
               ORDER BY id DESC
               LIMIT ?"""

    rows = db.query_database(query, (board, limit))
    return [] if not rows else [Post.from_dict(row) for row in rows]


def insert_post(board: str, creator: str, title: str, body: str, is_link: bool) -> Post:
    stmt = """INSERT
              INTO Post(board, creator, title, body, is_link, timestamp)
              VALUES (?, ?, ?, ?, ?, ?)"""

    timestamp = datetime.timestamp(datetime.now())

    row_id = db.modify_database(stmt, (board, creator, title, body, is_link, timestamp))

    # Since we just executed an INSERT statement,
    # we know [modify_database] returned an integer.
    assert row_id is not None

    return Post(row_id, board, creator, title, body, is_link, timestamp)


# Comment
def select_comment(id: int) -> Comment | None:
    query = """SELECT id, post, creator, body, timestamp, parent
               FROM Comment
               WHERE id = ?"""

    rows = db.query_database(query, (id,))
    return None if not rows else Comment.from_dict(rows[0])


def select_comments(post: int) -> list[Comment]:
    query = """SELECT id, post, creator, body, timestamp, parent
               FROM Comment
               WHERE post = ?"""

    rows = db.query_database(query, (post,))
    return [] if not rows else [Comment.from_dict(row) for row in rows]


def insert_comment(
    post: int,
    creator: str,
    body: str,
    parent: int | None,
) -> Comment | None:
    stmt = """INSERT
              INTO Comment(post, creator, body, timestamp, parent)
              VALUES (?, ?, ?, ?, ?)"""

    timestamp = datetime.timestamp(datetime.now())

    row_id = db.modify_database(stmt, (post, creator, body, timestamp, parent))
    assert row_id is not None

    return Comment(row_id, post, creator, body, timestamp, parent)
