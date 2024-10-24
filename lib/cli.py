# lib/cli.py

import click
from models import initialize_db
from models.genre import Genre
from models.book import Book
from helpers import format_genre_output, format_book_output

# Add @click.pass_context to pass the context (ctx) to the cli function
@click.group(invoke_without_command=True)
@click.pass_context
def cli(ctx):
    if ctx.invoked_subcommand is None:
        click.echo(ctx.get_help())

# add genre
@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    """Add a new genre."""
    try:
        genre = Genre.create(name)
        click.echo(f"Genre '{genre.name}' added successfully with ID {genre.id}.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# add book
@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author', prompt='Book author', help='The author of the book.')
@click.option('--genre_name', prompt='Genre name', help='The name of the genre for this book.')  # Changed prompt label to genre_name
def add_book(title, author, genre_name):
    genre = Genre.find_by_name(genre_name)
    if genre:
        genre_id = genre[0]
        try:
            Book.add_book(title, author, genre_id)
            click.echo(f"Book '{title}' by {author} added to genre '{genre_name}'.")
        except Exception as e:
            click.echo(f"Error: {str(e)}")
    else:
        click.echo(f"Error: Genre '{genre_name}' not found. Please add the genre first.")

# show available genres
@click.command()
def show_genres():
    genres = Genre.get_all_genres()
    if genres:
        for genre in genres:
            click.echo(format_genre_output(genre))
    else:
        click.echo("No genres have been added.")

# show books by genre
@click.command()
@click.option('--genre_name', prompt='Genre name', help='The name of the genre to show books from.')
def show_books(genre_name):
    try:
        genre = Genre.find_by_name(genre_name)
        if genre:
            genre_id = genre[0]
            books = Book.get_books_by_genre(genre_id)
            if books:
                for book in books:
                    click.echo(format_book_output(book))
            else:
                click.echo(f"No books found for genre '{genre_name}'.")
        else:
            click.echo(f"Genre '{genre_name}' not found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# delete genre
@click.command()
@click.option('--genre_name', prompt='Genre name', help='The name of the genre to delete.')
def delete_genre(genre_name):
    try:
        genre = Genre.find_by_name(genre_name)
        if genre:
            genre_id = genre[0]
            Genre.delete_genre(genre_id)
            click.echo(f"Genre '{genre_name}' deleted.")
        else:
            click.echo(f"Genre '{genre_name}' not found.")
    except Exception as e:
        click.echo(f"Error: {str(e)}")

# Register the commands
cli.add_command(add_genre)
cli.add_command(add_book)
cli.add_command(show_genres)
cli.add_command(show_books)
cli.add_command(delete_genre)

if __name__ == "__main__":
    initialize_db()
    cli()