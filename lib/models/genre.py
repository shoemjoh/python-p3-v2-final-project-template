import sqlite3
from models import CONN, CURSOR

class Genre:

    _genres = {}

    def __init__(self, name):
        self.name = name
        self.id = None
        Genre._genres[self.name] = self

    #add new genre to database
    @classmethod
    def add_genre(cls, name):
        if name in cls._genres:
            print(f"Error: Genre '{name}' already exists.")
            return
        genre = cls(name)
        sql = """
            INSERT INTO genres (name) VALUES (?)
        """
        try:
            CURSOR.execute(sql, (name,))
            CONN.commit()
            genre.id = CURSOR.lastrowid
            print(f"Genre '{name}' added successfully!")
        except sqlite3.IntegreityError:
            print(f"Error: Genre '{name}' already exists in database.")
    
    #get all genres
    @classmethod
    def get_all_genres(cls):
        sql = """
        SELECT * FROM genres
        """
        CURSOR.execute(sql)
        genres = CURSOR.fetchall()
        return genres
    
    #delete a genre
    @classmethod
    def delete_genre(cls, genre_id):
        sql = """
            DELETE FROM genres WHERE id = ?
        """
        CURSOR.execute(sql, (genre_id,))
        CONN.commit()
        cls._genres = [g for g in cls._genres if g.id != genre_id]
        print(f"GENRE ID {genre_id} deleted.")

    #find a genre by name
    @classmethod
    def find_by_name(cls, name):
        sql = """
        SELECT * FROM genres WHERE name = ?
        """
        CURSOR.execute(sql, (name,))
        genre = CURSOR.fetchone()
        return genre