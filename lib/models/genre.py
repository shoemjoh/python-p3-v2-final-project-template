from . import CONN, CURSOR

class Genre:
    all = {}

    def __init__(self, name, id=None):
        self.id = id
        self.name = name

    def __repr__(self):
        return f"<Genre {self.id}: {self.name}>"

    @property
    def name(self):
        return self._name

    @name.setter
    def name(self, name):
        if isinstance(name, str) and len(name) > 0:
            self._name = name
        else:
            raise ValueError("Name must be a non-empty string")

    def save(self):
        if self.id is None:
            sql = "INSERT INTO genres (name) VALUES (?)"
            CURSOR.execute(sql, (self.name,))
            CONN.commit()
            self.id = CURSOR.lastrowid
        else:
            sql = "UPDATE genres SET name = ? WHERE id = ?"
            CURSOR.execute(sql, (self.name, self.id))
            CONN.commit()

        type(self).all[self.id] = self

    @classmethod
    def create(cls, name):
        genre = cls(name)
        genre.save()
        return genre

    @classmethod
    def instance_from_db(cls, row):
        genre = cls.all.get(row[0])
        if genre:
            genre.name = row[1]
        else:
            genre = cls(row[1], id=row[0])
            cls.all[genre.id] = genre
        return genre

    @classmethod
    def find_by_id(cls, id):
        sql = "SELECT * FROM genres WHERE id = ?"
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_name(cls, name):
        sql = "SELECT * FROM genres WHERE name = ?"
        row = CURSOR.execute(sql, (name,)).fetchone()
        return cls.instance_from_db(row) if row else None

    def delete(self):
        sql = "DELETE FROM genres WHERE id = ?"
        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    # will call this on capital G Genre (class method)
    # Ruby on rails is the best ORM worked with
    # don't violate the separation of responsibilities principle
    # single source of truth - critical

    def books(self):
        from .book import Book

        sql = "SELECT * FROM books WHERE genre_id = ?"
        CURSOR.execute(sql, (self.id,))

        rows = CURSOR.fetchall()
        return [Book.instance_from_db(row) for row in rows] 

    @classmethod
    def get_all(cls):
        sql = "SELECT * FROM genres"
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]
