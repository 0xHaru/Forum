import sqlite3
from typing import Any

from flask import current_app

DBRow = dict[str, Any]
DBError = sqlite3.Error

# Links:
#   - https://flask.palletsprojects.com/en/2.0.x/patterns/sqlite3/#easy-querying
def dictionarify(cursor: sqlite3.Cursor, row: tuple[Any, ...]) -> DBRow:
    """Create a dictionary using the column names from the cursor
    description as keys and the row elements as values."""

    return dict((cursor.description[i][0], value) for i, value in enumerate(row))


def query_database(query: str, args: tuple[Any, ...] = ()) -> list[DBRow]:
    """Given a SQL query and its arguments, it executes the query
    and returns the matching rows."""

    connection = sqlite3.connect(current_app.config.get("DB_PATH"))  # type: ignore
    connection.row_factory = dictionarify

    cursor = connection.cursor()
    cursor.execute(query, args)

    rows = cursor.fetchall()

    cursor.close()
    connection.close()

    return rows


def modify_database(statement: str, args: tuple[Any, ...] = ()) -> int | None:
    """Executes a given SQL statement with 
    its arguments. If the statement is an 
    INSERT, then the ID of the inserted row
    is returned, None otherwise."""

    connection = sqlite3.connect(current_app.config.get("DB_PATH"))  # type: ignore

    # Enable foreign key constraints
    # https://www.sqlitetutorial.net/sqlite-foreign-key/
    connection.execute("PRAGMA foreign_keys = ON")
    cursor = connection.cursor()

    try:
        cursor.execute(statement, args)
        connection.commit()
    except sqlite3.Error as e:
        cursor.close()
        connection.close()
        raise sqlite3.Error(e)

    last_row_id = cursor.lastrowid

    cursor.close()
    connection.close()

    # If the current statement wasn't an INSERT, then
    # [last_row_id] doesn't refer to this statement
    # and we need to return [None].

    just_exec_an_insert = statement.strip()[:6].upper() == 'INSERT' # Hacky!

    if just_exec_an_insert:
        return last_row_id
    return None