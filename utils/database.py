books = []

def add_book(name, author):
    books.append({
        'name': name,
        'author': author
    })
    
    print('Book add!! ')


def list_book():
    for book in books:
        print(f'Name: {book["name"]}')
        print(f'Author: {book["author"]}') 
    
    
def read_book(name):
    for book in books:
        if name == book['name']:
            print(f'Name: {book["name"]}')
            print(f'Author: {book["author"]}')
                

def delete_book(name):
    for book in books:
        if name == book['name']:
            books.remove(book)
    
    print('Book deleted!')