import sys
from threading import Thread
import json
from book import Book
import random
from utils import *
import os

# TO DO LIST
# Add date

SHELF_PATH = 'shelf.json'
shelf = []

def getbooks(path):
        if os.path.exists(SHELF_PATH):
            with open(path, 'r') as shelf_file:

                books = json.load(shelf_file)
                shelf.clear()
                for book in books:
                    book_deatils = books[book]
                    
                    shelf.append(Book(book_deatils['id'], book_deatils['title'], book_deatils['author'],book_deatils['copies'], book_deatils['available_copies']))
    
getting_books = Thread(target=getbooks, args=(SHELF_PATH,))
getting_books.start()

def view_all_books():
        print('available books'.title())
        shelf = []
        with open(SHELF_PATH, 'r') as shelf_file:
            books = json.load(shelf_file)   
            for book in books:
                book_details = books[book]
                shelf.append(Book(book_details['id'], book_details['title'], book_details['author'], book_details['copies'], book_details['available_copies']))
        display_books(shelf) if len(shelf) > 1 else print('Émpty')
        return_prompt()
    

def display_books(shelf):
    print()
    for book in shelf:
        print(f'ID: {book.id}', )
        print(f'Title: {book.title.title()}', )
        print(f'Aurthor: {book.author.title()}', )
        print()

def search_book():
    search_phrase = str_input('Enter book Title or Aurthor')
    search_shelf = []
    with open(SHELF_PATH, 'r') as shelf_file:
        books = json.load(shelf_file)
        for book in books: 
            book_details = books[book]
            if book_details['title'] == search_phrase.lower() or book_details['author'] == search_phrase.lower():
                shelf.append(Book(book_details['id'], book_details['title'], book_details['author'], book_details['copies'], book_details['available_copies']))
        if not len(search_shelf):
            print('Book not found')
        else: 
            display_books(search_shelf)
        return_prompt()

def add_book():
    book_title = str_input('Enter book title').lower().strip()
    book_author = str_input('Enter book aurthor').lower().strip()
    exists = False
    shelf = []
    with open(SHELF_PATH, 'r') as shelf_file:
        books = json.load(shelf_file)
        for book in books:
            book_details = books[book]
            if book_details['title'] == book_title.lower() and book_details['author'] == book_title.lower():
                exists = True
            shelf.append(Book(book_details['id'], book_details['title'], book_details['author'], book_details['copies'], book_details['available_copies']))
    with open(SHELF_PATH, 'w') as shelf_file:
        shelf_dict = {}
        if not exists:
            for book in shelf:
                shelf_dict.update({ book.id: book.get_dict()})
            while True:
                id = generate_id('b',5)
                if not shelf_dict.get(id): break
            shelf_dict.update({id : Book.create_dict(id=id, title=book_title, author=book_author)})  
        else:
            for book in shelf:
                if book.author == book_author.lower() and book.title == book_title.lower():
                    book.copies += 1
                shelf_dict.update({ book.id: book.get_dict()})
        json.dump(shelf_dict, shelf_file, indent=5)

def register_member():
    first_name = str_input('Enter your first name')
    last_name = str_input('Enter your last name')

def main():
    print('='*30)
    print('Libarary management system'.upper().center(30,' '))
    print('='*30)
    while True :
        print('1. View all books\n2. Search for a book\n3. Add a new book\n4. Register a member\n5. Borrow a book\n6. Return a book\n7. View borrowing records\n8. View overdue books\n9. Exit\n')
        choice = int_input('Enter your choice',1,10)
        match choice:
            case 1:
                view_all_books()
            case 2:
                search_book()
            case 3:
                add_book()
            case 4:
                register_member()
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