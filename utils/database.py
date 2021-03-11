import sqlite3


books_file = 'books.txt'


def create_book_table():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute('CREATE TABLE IF NOT EXISTS books(name text primary key, author text, read integer)')
    
    connection.commit()
    connection.close()
    
    
def add_book(name, author):
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute(f'INSERT INTO books VALUES(?, ?, 0)', (name, author))
    
    connection.commit()
    connection.close()


def list_book():
    connection = sqlite3.connect('data.db')
    cursor = connection.cursor()
    
    cursor.execute(f'SELECT * FROM books')
    books = [
        {'name': row[0], 'author': row[1], 'read': row[2]}
        for row in cursor.fetchall()
    ]
    
    connection.close()
    
    return books
    
    
def read_book(name):
    books = list_book()
    
    for book in books:
        if name == book['name']:
            book['read'] = 1
    
    _save_all_books(books)


def _save_all_books(books):
    with open(books_file, 'w') as file:
        for book in books:
            file.write(f'{book["name"]},{book["author"]},{book["read"]}\n')
            

def delete_book(name):
    books = list_book()
    
    books = [
        book
        for book in books
        if book['name'] != name
    ]
    
    _save_all_books(books)
    