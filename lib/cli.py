import click
import sqlite3
from models import initialize_db
from models.genre import Genre
from models.book import Book
from helpers import format_genre_output, format_book_output, exit_program

# Add genre
def add_genre():
    name = input("Genre name: ")
    try:
        genre = Genre.create(name)
        click.echo(f"Genre '{genre.name}' added successfully.")
    except sqlite3.IntegrityError:
        click.echo(f"Error: Genre '{name}' already exists.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")


    # this is duplicative to what we're already doing in the Book model, you keep going back to genre_name which is not efficient at all.
    # once I have the genre object, double check everywhere you call Genre.find_by_name
    # in the next phase, react frontend will replace the CLI and helpers. It should do minimal fetching.
    # frontend needs to be smart about when it needs to ask for information from the backend
    # fix this duplicative code, and add the .books
    # you'll use an ORM in phase 4 that does this for you!
    # would have printed out the existing genres to pick from

    # fundamentals of python, list comprehensions, decorators
    # object orientation: do you understand what an object is, self, class method and instance methods
    # don't call a class an instance or an instance a class
    # request response flow, cli and helpers are the view
    # genres = Genre.get_all()

# Add book
def add_book():
    title = input("Book title: ")
    author = input("Book author: ")
    genre_name = input("Genre name: ")

    try:
        book = Book.create(title, author, genre_name)
        click.echo(f"Book '{book.title}' by {book.author} added to genre '{genre_name}'.")
    except ValueError as e:
        click.echo(f"Error: {str(e)}")
    except sqlite3.IntegrityError:
        click.echo(f"Error: Book '{title}' already exists.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")
    # genre = Genre.find_by_name(genre_name)
    # if genre:
    #     try:
    #         book = Book.create(title, author, genre_name)
    #         click.echo(f"Book '{book.title}' by {book.author} added to genre '{genre_name}'.")
    #     except sqlite3.IntegrityError:
    #         click.echo(f"Error: Book '{title}' already exists.")
    #     except Exception as e:
    #         click.echo(f"Error: {str(e)}")
    # else:
    #     click.echo(f"Error: Genre '{genre_name}' not found. Please add the genre first.")

# Show all genres
def show_genres():
    genres = Genre.get_all()
    if genres:
        for genre in genres:
            click.echo(format_genre_output(genre))
    else:
        click.echo("No genres have been added.")

# Show books by genre
def show_books():

    # want to just be able to call genres.books() to show the books associated with the genres. Instance method in the genre model.
    genre_name = input("Genre name: ")
        
    genre = Genre.find_by_name(genre_name)
    if genre:
        # books = Book.get_all()
        # filtered_books = [book for book in books if book.genre_id == genre.id]
        filtered_books = genre.books()
        if filtered_books:
            for book in filtered_books:
                click.echo(format_book_output(book))
        else:
            click.echo(f"No books found for genre '{genre_name}'.")
    else:
        click.echo(f"Genre '{genre_name}' not found.")

# Delete genre
def delete_genre():
    genre_name = input("Genre name: ")
        
    genre = Genre.find_by_name(genre_name)
    if genre:
        genre.delete()
        click.echo(f"Genre '{genre_name}' deleted.")
    else:
        click.echo(f"Genre '{genre_name}' not found.")

def delete_book():
    title = input("Book title to delete: ")
    try:
        Book.delete_by_title(title)
    except Exception as e:
        click.echo(f"Error: {str(e)}")

def show_menu():
    click.echo("\nMain Menu:")
    click.echo("1. Add Genre")
    click.echo("2. Add Book")
    click.echo("3. Show All Genres")
    click.echo("4. Show Books by Genre")
    click.echo("5. Delete Genre")
    click.echo("6. Delete Book") 
    click.echo("0. Exit\n")

def handle_choice(choice):
    """Handle the user's menu choice."""
    try:
        if choice == '1':
            add_genre()
        elif choice == '2':
            add_book()
        elif choice == '3':
            show_genres()
        elif choice == '4':
            show_books()
        elif choice == '5':
            delete_genre()
        elif choice == '6':
            delete_book()
        elif choice == '0':
            exit_program()
        else:
            click.echo("Invalid choice. Please select a valid option.")
    except Exception as e:
        click.echo(f"An error occurred: {str(e)}")

def main_loop():
    while True:
        try:
            show_menu()
            choice = input("Select an option: ")
            handle_choice(choice)
            input("\nPress Enter to return to the main menu...")
        except KeyboardInterrupt:
            click.echo("\nExiting program.")
            exit_program()

if __name__ == "__main__":
    initialize_db()
    main_loop()
