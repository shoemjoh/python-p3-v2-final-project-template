import sqlite3
from __init__  import CONN, CURSOR

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