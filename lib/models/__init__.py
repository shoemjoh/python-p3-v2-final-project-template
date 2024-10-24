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

    CONN.commit()
