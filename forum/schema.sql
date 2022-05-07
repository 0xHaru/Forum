CREATE TABLE IF NOT EXISTS User (
    username                    VARCHAR(32) PRIMARY KEY,
    hash                        VARCHAR(32) NOT NULL,
    salt                        VARCHAR(16) NOT NULL,
    email                       VARCHAR(256) UNIQUE,
    website                     VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS Board (
    name                        VARCHAR(4) PRIMARY KEY,
    full_name                   VARCHAR(32) UNIQUE,
    description                 VARCHAR(512)
);

CREATE TABLE IF NOT EXISTS Post (
    id                          INTEGER AUTOINCREMENT PRIMARY KEY,
    board                       VARCHAR(4) NOT NULL,
    title                       VARCHAR(128) NOT NULL,
    body                        VARCHAR(8192) NOT NULL,
    is_link                     BOOLEAN NOT NULL,
    timestamp                   INTEGER NOT NULL, -- UNIX TIMESTAMP

    FOREIGN KEY(board)
        REFERENCES Board(name)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);

CREATE TABLE Comment (
    id                          INTEGER AUTOINCREMENT PRIMARY KEY,
    post                        INTEGER NOT NULL,
    parent                      INTEGER,
    body                        VARCHAR(4096) NOT NULL,
    timestamp                   INTEGER NOT NULL,

    FOREIGN KEY(post)
        REFERENCES Post(name)
            ON UPDATE CASCADE
            ON DELETE CASCADE,

    FOREIGN KEY(parent)
        REFERENCES Comment(name)
            ON UPDATE CASCADE
            ON DELETE CASCADE
);
