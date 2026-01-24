import sqlite3


def create_table():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    cursor.execute("""
        CREATE TABLE IF NOT EXISTS books (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            author TEXT,
            publication_year INTEGER,
            genre TEXT,
            number_of_pages INTEGER,
            number_of_copies INTEGER
        )
    """)

    conn.commit()
    conn.close()


def insert_books():
    conn = sqlite3.connect("library.db")
    cursor = conn.cursor()

    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("Animal Farm", "George Orwell", 1945, "Political satire", 112, 4),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 309, 7),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 6),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Dystopia", 249, 3),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Novel", 277, 2),
        ("To Kill a Mockingbird", "Harper Lee", 1960, "Novel", 281, 4),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 5),
        ("Moby-Dick", "Herman Melville", 1851, "Adventure", 635, 1),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological novel", 671, 2)
    ]

    cursor.executemany("""
        INSERT INTO books (
            name, author, publication_year, genre,
            number_of_pages, number_of_copies
        ) VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_books()
    print("Таблица создана и книги добавлены.")
