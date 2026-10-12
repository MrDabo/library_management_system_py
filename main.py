import sys
from threading import Thread
import json
from book import Book

shlef_path = 'shelf.json'
shelf = []

def getbooks(path):
    with open(path, 'r') as shelf_file:
        books = json.load(shelf_file)
        for book in books:
            book_deatils = books[book]
            shelf.append(Book(book_deatils['id'], book_deatils['title'], book_deatils['aurthor'],book_deatils['copies'], book_deatils['available_copies']))
   

getting_books = Thread(target=getbooks, args=(shlef_path,))
getting_books.start()

def view_all_books():
    print('available books\n'.title())
    getting_books.join()
    view_books(shelf)
    

def view_books(shelf):
    print()
    for book in shelf:
        print(f'ID: {book.id}', )
        print(f'Title: {book.title.title()}', )
        print(f'Aurthor: {book.aurthor.title()}', )
        print()

def search_book():
    search_phrase = str_input('Enter book title or aurthor')
    getting_books.join()
    search_shelf = []
    for book in shelf: 
        if book.title.lower() == search_phrase.lower() or book.aurthor.lower() == search_phrase.lower():
            search_shelf.append(book)
    if not len(search_phrase):
        print('Book not found')
    else: 
        view_books(search_shelf)

def add_book():
    book_title = str_input('Enter book title')
    book_aurthor = str_input('Enter book aurthor')
    exists = False
    for book in shelf:
        if book.aurthor.lower() == book.aurthor.lower() and book.title.lower() == book_title.lower():
            exists = True
    if not exists: 
       pass
    else:
        pass

def int_input(prompt, start, end):
    while True: 
        input_value = input(f'{prompt}: ')
        if not input_value.isdigit():
            print('Please enter only numeric characters')
        else:
            input_value = int(input_value)
        if not start <= input_value <= end:
            print(f'Please enter a value between {start} and {end}')
        else:
            break
    return input_value

def str_input(prompt): 
    while True:
        input_value = input(f'{prompt}: ')
        if not input_value:
            print(f'Please {prompt.lower()}')
        else: break
    return input_value
    

def main():
    print('='*30)
    print('Libarary management system'.upper().center(30,' '))
    print('='*30)
    print('\n1. View all books\n2. Search for a book\n3. Add a new book\n4. Register a member\n5. Borrow a book\n6. Return a book\n7. View borrowing records\n8. View overdue books\n9. Exit\n')
    while True :
        choice = int_input('Enter your choice',1,10)
        match choice:
            case 1:
                view_all_books()
            case 2:
                search_book()
            case 3:
                add_book()
                pass
            case 4:
                pass
            case 5:
                pass
            case 6:
                pass
            case 7:
                pass
            case 8:
                pass
            case 9:
                break
    sys.exit('Bye!')

if __name__=='__main__':
    main()