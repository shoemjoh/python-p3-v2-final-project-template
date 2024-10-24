import click
from models import initialize_db
from models.genre import Genre
from models.book import Book
from helpers import format_genre_output, format_book_output

@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    """Book Collection Manager CLI."""
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

# Add genre
@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    """Add a new genre."""
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
    """Add a new book."""
    genre = Genre.find_by_name(genre_name)
    if genre:
        try:
            book = Book.create(title, author, genre.id)
            click.echo(f"Book '{book.title}' by {book.author} added to genre '{genre.name}'.")
        except Exception as e:
            click.echo(f"Error: {str(e)}")
    else:
        click.echo(f"Error: Genre '{genre_name}' not found. Please add the genre first.")

# Show all genres
@click.command()
def show_genres():
    """Show all genres."""
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
    """Show all books for a specific genre."""
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
    """Delete a genre by its name."""
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

if __name__ == "__main__":
    initialize_db()
    cli()
