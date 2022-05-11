@dataclass
class User:
    username: str
    email: str
    website: str


@dataclass
class Board:
    name: str
    full_name: str | None


__users = [
    (User("cozis", "cozis@gmail.com", "cozis.github.io"), "cozis-pwd"),
    (User("0xharu", "haru@hotmail.com"), "harus-pwd"),
]

__boards = [
    Board("prog", "Programmazione"),
    Board("tech", "Tecnologia"),
    Board("misc", "Miscellanea"),
]


def __find_mock_user_from_username(username) -> User | None:

    for user, password in __users:

        if user.username == username:
            return user, password

    return None


def get_user(username: str, password: str | None) -> User | None:

    # Find username and password
    mock_user, mock_password = __find_mock_user_from_username(username)

    if mock_user is None:
        # There's no such user.
        return None

    # If the caller didn't specify a password,
    # then the search is done.
    if password is None:
        return mock_user

    # Not only the user with the given username
    # must exist, but it must exist with a
    # specific password.
    if password == mock_password:
        return mock_user

    # Password didn't match.
    return None


def new_user(user: User, password: str) -> None:

    # Make sure the user doesn't exist already.
    found, _ = __find_mock_user_from_username(user.username)

    if found:
        raise "Username already in use"

    __users.append((user, password))


def get_board(name: str) -> Board | None:

    for board in __boards:
        if name == board.name:
            return board
    return None
