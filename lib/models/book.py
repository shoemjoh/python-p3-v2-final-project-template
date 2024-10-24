import sqlite3
from __init__  import CONN, CURSOR

class Book:
    def __init__(self, title, author, genre_id):
        self.title = title
        self.author = author
        self.genre_id = genre_id

    #add a book to the table books
    @classmethod
    def add_book (cls, title, author, genre_id):
        sql = '''
        INSERT INTO books (title, author, genre_id) VALUES (?, ?, ?)
        '''
        CURSOR.execute(sql, (title, author, genre_id))
        CONN.commit()
        print(f"Book '{title}' by {author} added to genre ID {genre_id}")

    # get all the books of a certain genre
    @classmethod
    def get_books_by_genre(cls, genre_id):
        sql = '''
        SELECT * FROM books WHERE genre_id = ?
        '''
        CURSOR.execute(sql, (genre_id,))
        books = CURSOR.fetchall()
        return books
    
    @classmethod
    def delete_books(cls, book_id):
        sql = """
        DELETE FROM books WHERE book_id = ?
        """
        CURSOR.execute(sql, (book_id,))
        CONN.commit()
        print(f"Book ID {book_id} deleted.")

    @classmethod
    def find_by_title(cls, title):
        sql = """
        SELECT * FROM books WHERE title = ?
        """
        CURSOR.execute(sql, (title,))
        book = CURSOR.fetchone()
        return book