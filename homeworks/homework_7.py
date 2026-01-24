import sqlite3


DB_NAME = "library.db"


def create_table():
    conn = sqlite3.connect(DB_NAME)
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
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    books = [
        ("1984", "George Orwell", 1949, "Dystopia", 328, 5),
        ("Brave New World", "Aldous Huxley", 1932, "Dystopia", 311, 4),
        ("Fahrenheit 451", "Ray Bradbury", 1953, "Sci-Fi", 249, 6),
        ("The Hobbit", "J.R.R. Tolkien", 1937, "Fantasy", 310, 8),
        ("Harry Potter", "J.K. Rowling", 1997, "Fantasy", 450, 10),
        ("The Catcher in the Rye", "J.D. Salinger", 1951, "Novel", 277, 3),
        ("The Great Gatsby", "F. Scott Fitzgerald", 1925, "Novel", 180, 4),
        ("Moby Dick", "Herman Melville", 1851, "Adventure", 635, 2),
        ("War and Peace", "Leo Tolstoy", 1869, "Historical", 1225, 1),
        ("Crime and Punishment", "Fyodor Dostoevsky", 1866, "Psychological", 671, 3),
    ]

    cursor.executemany("""
        INSERT INTO books (
            name, author, publication_year,
            genre, number_of_pages, number_of_copies
        )
        VALUES (?, ?, ?, ?, ?, ?)
    """, books)

    conn.commit()
    conn.close()


def get_all_books():
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    conn.close()
    return books


def update_book_title(book_id, new_title):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("""
        UPDATE books
        SET name = ?
        WHERE id = ?
    """, (new_title, book_id))

    conn.commit()
    conn.close()


def delete_book(book_id):
    conn = sqlite3.connect(DB_NAME)
    cursor = conn.cursor()

    cursor.execute("DELETE FROM books WHERE id = ?", (book_id,))

    conn.commit()
    conn.close()


if __name__ == "__main__":
    create_table()
    insert_books()

    print(" Все книги:")
    for book in get_all_books():
        print(book)

    print("\n Изменяем название книги с id = 1")
    update_book_title(1, "Nineteen Eighty-Four")

    print("\n Удаляем книгу с id = 2")
    delete_book(2)

    print("\n Книги после изменений:")
    for book in get_all_books():
        print(book)
