# lib/cli.py

import click
from models import initialize_db
from models.genre import Genre
from models.book import Book
from helpers import validate_genre_id, validate_book_id, format_genre_output, format_book_output

@click.group()
def cli():
    """Book Collection Manager CLI."""
    pass

#add genre
@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    """Add a new genre."""
    try:
        Genre.add_genre(name)
    except Exception as e:
        click.echo(f"Error: {str(e)}")

#add book
@click.command()
@click.option('--title', prompt='Book title', help='The title of the book.')
@click.option('--author', prompt='Book author', help='The author of the book.')
@click.option('--genre_id', prompt='Genre Name', help='The ID of the genre for this book.')
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



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
