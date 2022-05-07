from typing import Any

from flask_login import UserMixin


class User(UserMixin):  # type: ignore
    def __init__(
        self,
        username: str,
        password: str | None,
        email: str | None,
        website: str | None,
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
    def __init__(self, name: str, full_name: str | None, description: str | None):
        self.name = name
        self.full_name = full_name
        self.description = description

    @staticmethod
    def from_dict(d: dict[str, str]) -> Any:
        name = d.get("name")
        full_name = d.get("full_name")
        description = d.get("description")

        return Board(name, full_name, description)  # type: ignore
