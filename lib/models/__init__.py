import sqlite3

#establish connection and create cursor
CONN = sqlite3.connect('library.db')
CURSOR = CONN.cursor()

#initialize the database
def initialize_db():
    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS genres (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL UNIQUE
        )
    ''')

    CURSOR.execute('''
        CREATE TABLE IF NOT EXISTS books (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        author TEXT NOT NULL,
        genre_id INTEGER, 
        FOREIGN KEY (genre_id) REFERENCES genres(id) ON DELETE SET NULL
        )
    ''')

CONN.commit()
