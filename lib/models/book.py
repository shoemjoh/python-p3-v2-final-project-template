from . import CONN, CURSOR
from models.genre import Genre

class Book:
    all = {}

    def __init__(self, title, author, genre_name, id=None):
        self.id = id
        self.title = title
        self.author = author
        genre = Genre.find_by_name(genre_name)
        if genre:
            self.genre_id = genre.id
        else:
            raise ValueError(f"Genre '{genre_name}' not found. Please add the genre first.")

    def __repr__(self):
        return f"<Book {self.id}: {self.title}, {self.author}, Genre ID: {self.genre_id}>"

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if isinstance(title, str) and len(title) > 0:
            self._title = title
        else:
            raise ValueError("Title must be a non-empty string")

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        if isinstance(author, str) and len(author) > 0:
            self._author = author
        else:
            raise ValueError("Author must be a non-empty string")

    def save(self):
        if self.id is None:
            sql = "INSERT INTO books (title, author, genre_id) VALUES (?, ?, ?)"
            CURSOR.execute(sql, (self.title, self.author, self.genre_id))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = "UPDATE books SET title = ?, author = ?, genre_id = ? WHERE id = ?"
            CURSOR.execute(sql, (self.title, self.author, self.genre_id, self.id))
            CONN.commit()

        type(self).all[self.id] = self

    @classmethod
    def create(cls, title, author, genre_name):
        book = cls(title, author, genre_name)
        book.save()
        return book

    @classmethod
    def instance_from_db(cls, row):
        """Create or retrieve a book instance from the database."""
        book = cls.all.get(row[0])
        if book:
            book.title = row[1]
            book.author = row[2]
            book.genre_id = row[3]
        else:
            genre_name = Genre.find_by_id(row[3]).name  
            book = cls(row[1], row[2], genre_name, id=row[0])
            cls.all[book.id] = book
        return book

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM books WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_title(cls, title):
        sql = "SELECT * FROM books WHERE title = ?"
        row = CURSOR.execute(sql, (title,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete(self):
        sql = "DELETE FROM books WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM books"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
