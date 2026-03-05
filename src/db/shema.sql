PRAGMA foreign_keys = ON;

CREATE TABLE IF NOT EXISTS authors (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    birth_year INTEGER,
    name TEXT
);

CREATE TABLE IF NOT EXISTS publisher (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    country TEXT,
    city TEXT,
    year_publisher TEXT
);

CREATE TABLE IF NOT EXISTS books (
    id INTEGER PRIMARY KEY AUTOINCREMENT,
    author_id INTEGER NOT NULL,
    namebook TEXT NOT NULL,
    genre TEXT,
    pages INTEGER,
    publisher_id INTEGER NOT NULL,
    FOREIGN KEY (author_id) REFERENCES authors (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE,
    FOREIGN KEY (publisher_id) REFERENCES publisher (id)
        ON DELETE RESTRICT
        ON UPDATE CASCADE
);
