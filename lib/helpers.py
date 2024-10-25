from models.genre import Genre
from models.book import Book

def validate_genre_id(genre_id):
    genre = Genre.find_by_id(genre_id)
    if genre:
        return genre
    else:
        raise ValueError(f"No genre found with ID {genre_id}.")

def validate_book_id(book_id):
    book = Book.find_by_id(book_id)
    if book:
        return book
    else:
        raise ValueError(f"No book found with ID {book_id}.")

def format_genre_output(genre):
    return f"{genre.name}"

def format_book_output(book):
    genre_name = Genre.find_by_id(book.genre_id).name  
    return f"'{book.title}' by {book.author} (Genre: {genre_name})"

def exit_program():
    print("Goodbye!")
    exit()

def list_genres():
    genres = Genre.get_all()
    if not genres:
        return "No genres available."
    
    output = "\nAvailable Genres:\n"
    for i, genre in enumerate(genres, start=1):
        output += f"{i}. {genre.name} (ID: {genre.id})\n"
    return output

def list_books_by_genre(genre_name):
    genre = Genre.find_by_name(genre_name)
    if not genre:
        return f"Genre '{genre_name}' not found."
    
    books = Book.get_all()
    books_in_genre = [book for book in books if book.genre_id == genre.id]
    
    if not books_in_genre:
        return f"No books found for genre '{genre_name}'."
    
    output = f"\nBooks in Genre '{genre.name}':\n"
    for i, book in enumerate(books_in_genre, start=1):
        output += f"{i}. '{book.title}' by {book.author}\n"
    return output
