import sqlite3
from . import CONN, CURSOR

class Genre:
    def __init__(self, name):
        self.name = name

    #add new genre to database
    @classmethod
    def add_genre(cls, name):
        sql = """
            INSERT INTO genres (name) VALUES (?)
        """
        try:
            CURSOR.execute(sql, (name,))
            CONN.commit()
            print(f"Genre '{name}' added successfully!")
        except sqlite3.IntegreityError:
            print(f"Error: Genre '{name}' already exists.")
    
    #get all genres
    def get_all_genres(cls):
        sql = """
        SELECT * FROM genres
        """
        CURSOR.execute(sql)
        genres = CURSOR.fetchall()
        return genres
        