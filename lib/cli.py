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

# Add Genre
@click.command()
@click.option('--name', prompt='Genre name', help='The name of the genre.')
def add_genre(name):
    """Add a new genre."""
    try:
        Genre.add_genre(name)
    except Exception as e:
        click.echo(f"Error: {str(e)}")



def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Some useful function")


if __name__ == "__main__":
    main()
