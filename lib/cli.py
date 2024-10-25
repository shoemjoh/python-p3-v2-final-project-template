import click
from models import initialize_db
from models.genre import Genre
from models.book import Book
from helpers import format_genre_output, format_book_output, exit_program

@click.group()
def cli():
    pass

# Add genre
@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    try:
        genre = Genre.create(name)
        click.echo(f"Genre '{genre.name}' added successfully with ID {genre.id}.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Add book
@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author', prompt='Book author', help='The author of the book.')
@click.option('--genre_name', prompt='Genre name', help='The name of the genre for this book.')
def add_book(title, author, genre_name):
    genre = Genre.find_by_name(genre_name)
    if genre:
        try:
            book = Book.create(title, author, genre_name)
            click.echo(f"Book '{book.title}' by {book.author} added to genre '{genre_name}'.")
        except Exception as e:
            click.echo(f"Error: {str(e)}")
    else:
        click.echo(f"Error: Genre '{genre_name}' not found. Please add the genre first.")

# Show all genres
@click.command()
def show_genres():
    genres = Genre.get_all()
    if genres:
        for genre in genres:
            click.echo(format_genre_output(genre))
    else:
        click.echo("No genres have been added.")

# Show books by genre
@click.command()
@click.option('--genre_name', prompt='Genre name', help='The name of the genre to show books from.')
def show_books(genre_name):
    genre = Genre.find_by_name(genre_name)
    if genre:
        books = Book.get_all()
        filtered_books = [book for book in books if book.genre_id == genre.id]
        if filtered_books:
            for book in filtered_books:
                click.echo(format_book_output(book))
        else:
            click.echo(f"No books found for genre '{genre_name}'.")
    else:
        click.echo(f"Genre '{genre_name}' not found.")

# Delete genre
@click.command()
@click.option('--genre_name', prompt='Genre name', help='The name of the genre to delete.')
def delete_genre(genre_name):
    genre = Genre.find_by_name(genre_name)
    if genre:
        genre.delete()
        click.echo(f"Genre '{genre_name}' deleted.")
    else:
        click.echo(f"Genre '{genre_name}' not found.")

# Register commands
cli.add_command(add_genre)
cli.add_command(add_book)
cli.add_command(show_genres)
cli.add_command(show_books)
cli.add_command(delete_genre)

def show_menu():
    click.echo("\nMain Menu:")
    click.echo("1. Add Genre")
    click.echo("2. Add Book")
    click.echo("3. Show All Genres")
    click.echo("4. Show Books by Genre")
    click.echo("5. Delete Genre")
    click.echo("0. Exit\n")

def handle_choice(choice):
    """Handle the user's menu choice."""
    if choice == '1':
        cli(['add-genre'])
    elif choice == '2':
        cli(['add-book'])
    elif choice == '3':
        cli(['show-genres'])
    elif choice == '4':
        cli(['show-books'])
    elif choice == '5':
        cli(['delete-genre'])
    elif choice == '0':
        exit_program()
    else:
        click.echo("Invalid choice. Please select a valid option.")
        
def main_loop():
    while True:
        show_menu()
        choice = input("Select an option: ")
        handle_choice(choice)

if __name__ == "__main__":
    initialize_db()
    main_loop()
