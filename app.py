from utils import database


USER_CHOICE = """
Enter:
- 'a' to add new book
- 'l' to list all books
- 'r' to mark a book as read
- 'd' to delete a book
- 'q' to quit

Your choice: """


def add_book():
    name = input('Enter the name of the book: ')
    author = input('Enter the author of the book: ')
    
    database.add_book(name=name, author=author)
    

def list_book():
    books = database.list_book()
    
    for book in books:
        read = 'YES' if book['read'] == '1' else 'NO'
        print(f'{book["name"]} by {book["author"]}, read: {read}')


def read_book():
    name = input('Enter the name of the book: ')

    database.read_book(name=name)


def delete_book():
    name = input('Enter the name of the book: ')
    
    database.delete_book(name=name)
    

PROMPT_FUNCTIONS = {
    'a': add_book,
    'l': list_book,
    'r': read_book,
    'd': delete_book,
}


def menu():
    database.create_book_table()
    try:
        user_input = input(USER_CHOICE).lower()[0]
    
        while user_input != 'q':
            PROMPT_FUNCTIONS[user_input]()
            user_input = input(USER_CHOICE).lower()[0]
    except:
        print('Unknown comand. Please try again')

menu()
