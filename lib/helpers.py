# lib/helpers.py
import sqlite3
from models import CONN, CURSOR

def validate_genre_id(genre_id):
    sql = """
    SELECT * FROM genres WHERE id = ?
    """
    CURSOR.execute(sql, (genre_id,))
    genre = CURSOR.fetchone()
    if genre:
        return genre
    else:
        raise ValueError(f"No genre found with ID {genre_id}.")
    
def validate_book_id(book_id):
    sql = """
    SELECT * FROM genres WHERE id = ?
    """
    CURSOR.execute(sql, (book_id,))
    book = CURSOR.fetchone()
    if book:
        return book
    else:
        raise ValueError(f"No book found with ID {book_id}.")

def format_genre_output(genre):
    return f"{genre[0]}: {genre[1]}"

def format_book_output(book):
    return f"{book[0]}: {book[1]} by {book[2]} (Genre ID: {book[3]})"



def exit_program():
    print("Goodbye!")
    exit()
