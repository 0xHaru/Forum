-- USERS

INSERT INTO User(username, password, email, website)
VALUES(
    "wutang",
    "pbkdf2:sha256:260000$Q4EB90heYtFW0JN9$29019d41dfcedb6e13f1472a566ca6b0113cede6a81739c9f066661b70304d31",
    "wutang@gmail.com",
    "wutang.com"
);

INSERT INTO User(username, password, email, website)
VALUES(
    "krazam",
    "pbkdf2:sha256:260000$1P5bidmlnudRxg2S$e885b238cfb6eddef50fbef7ec008a35626726cd86d3eafa9a89bbe1ee5156d7",
    "krazam@gmail.com",
    "krazam.com"
);

-- BOARDS

INSERT INTO Board(name, full_name, description)
VALUES("prog", "Programmazione", NULL);

INSERT INTO Board(name, full_name, description)
VALUES("tech", "Tecnologia", NULL);

INSERT INTO Board(name, full_name, description)
VALUES("math", "Matematica", NULL);

INSERT INTO Board(name, full_name, description)
VALUES("misc", "Miscellanea", NULL);

-- POSTS
