Library Manager CLI

Overview
The Library Manager CLI is a Python-based command-line application that allows users to manage a collection of books and their associated genres. The project utilizes SQLite for persistent data storage, ensuring that books and genres are retained between sessions. Users can add new genres, associate books with those genres, and retrieve or delete entries as needed.

This project demonstrates Object-Relational Mapping (ORM) in Python.

Features
- Add genres: Create new book genres (e.g., "Science Fiction", "Fantasy").
- Add books: Add books to a specific genre (e.g., "Dune" under "Science Fiction").
- View genres: List all available genres.
- View books by genre: Retrieve books under a specific genre.
- Delete genres: Remove genres and their associated books from the collection.
- Validation: Ensures uniqueness of genres and books (no duplicates allowed).

Key Files:

- cli.py: This file contains the core logic for the command-line interface. It provides a menu-driven interface that allows users to interact with the database by adding genres, adding books, viewing entries, and deleting records.
  
Models
  - genre.py: Defines the `Genre` class, which includes methods for creating, retrieving, and deleting genres.
  - book.py: Defines the `Book` class, which manages the book entries and their relationships to genres.
  
- helpers.py: Contains utility functions to validate inputs.

Data Models
The project has two main data models:
1. Genre: Represents a book genre (e.g., "Science Fiction").
2. Book: Represents a book, with attributes like title, author, and the genre it belongs to.

Relationship:
- One-to-many: A genre can have multiple books, but a book belongs to only one genre.

How to Run the Application
Prerequisites:
1. Ensure you have Python installed (preferably 3.8+).
2. Install `pipenv` for managing dependencies.

Steps:
Clone the repository**:
   ```bash
   git clone <repository-url>
   cd <repository-folder>