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

#show available genres
@click.command()
def show_genres():
    genres = Genre.get_all_genres()
    if genres:
        for genre in genres:
            click.echo(format_genre_output(genre))
    else:
        click.echo("No genres have been added.")

#show books
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