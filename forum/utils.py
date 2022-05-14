from urllib.parse import urlparse
from typing import Any
from flask import abort


def abort_if_falsy(resource: Any | None, status_code: int) -> None:
    if not resource:
        abort(status_code)


def is_url_valid(url: str) -> bool:
    # From: https://stackoverflow.com/questions/18423853/how-to-validate-url-and-redirect-to-some-url-using-flask
    try:
        result = urlparse(url)
        return all([result.scheme, result.netloc, result.path])
    except:
        return False
