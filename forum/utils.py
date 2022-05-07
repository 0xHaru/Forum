from typing import Any

from flask import abort


def abort_if_falsy(resource: Any | None, status_code: int) -> None:
    if not resource:
        abort(status_code)
