# Library Collection Manager CLI

## Overview
This project is a command-line application to manage a collection of books and their genres, built using Python and SQLite for database management.

## Features
- Add genres and books to the database.
- View all genres or books in a specific genre.
- Delete genres and books.
- Validate the existence of genres and books before actions.

## How to Run
1. Clone the repository.
2. Install dependencies using `pipenv install`.
3. Initialize the database and run the CLI:

   ```bash
   pipenv shell
   python lib/cli.py