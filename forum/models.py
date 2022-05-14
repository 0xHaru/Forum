from typing import Any

from flask_login import UserMixin


class User(UserMixin):  # type: ignore
    def __init__(
        self,
        username: str,
        password: str | None = None,
        email: str | None = None,
        website: str | None = None,
    ):
        self.id = username
        self.username = username
        self.password = password
        self.email = email
        self.website = website

    @staticmethod
    def from_dict(d: dict[str, str]) -> Any:
        username = d.get("username")
        password = d.get("password")
        email = d.get("email")
        website = d.get("website")

        return User(username, password, email, website)  # type: ignore


class Board:
    def __init__(
        self,
        name: str,
        full_name: str | None = None,
        description: str | None = None,
    ):
        self.name = name
        self.full_name = full_name
        self.description = description

    @staticmethod
    def from_dict(d: dict[str, str]) -> Any:
        name = d.get("name")
        full_name = d.get("full_name")
        description = d.get("description")

        return Board(name, full_name, description)  # type: ignore


class Post:
    def __init__(
        self,
        id: int,
        board: str,
        creator: str,
        title: str,
        body: str,
        is_link: bool,
        timestamp: int,
    ):
        self.id = id
        self.hex_id = hex(id)  # This isn't strictly necessary but
        # it's useful to cache it here.
        self.board = board
        self.creator = creator
        self.title = title
        self.body = body
        self.is_link = is_link
        self.timestamp = timestamp

    @staticmethod
    def from_dict(d: dict[str, Any]) -> Any:
        id = d.get("id")
        board = d.get("board")
        creator = d.get("creator")
        title = d.get("title")
        body = d.get("body")
        is_link = d.get("is_link")
        timestamp = d.get("timestamp")

        return Post(id, board, creator, title, body, is_link, timestamp)  # type: ignore


class Comment:
    def __init__(
        self,
        id: int,
        post: int,
        creator: str,
        body: str,
        timestamp: int,
        parent: int | None = None,
    ):
        self.id = id
        self.post = post
        self.creator = creator
        self.body = body
        self.timestamp = timestamp
        self.parent = parent

    @staticmethod
    def from_dict(d: dict[str, Any]) -> Any:
        id = d.get("id")
        post = d.get("post")
        creator = d.get("creator")
        body = d.get("body")
        timestamp = d.get("timestamp")
        parent = d.get("parent")

        return Comment(id, post, creator, body, timestamp, parent)  # type: ignore
