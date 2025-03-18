# Personal Library Manager

This project is a command-line application that helps users manage their personal book collections. Users can add, remove, search for books, display all books, and view basic library statistics. The program also saves the library to a file (`library.txt`) for persistence.

## Features
- Add books with attributes like Title, Author, Year, Genre, and Read Status.
- Remove books from the library by title.
- Search for books by title or author.
- Display all books in a neatly formatted view.
- View statistics such as:
  - Total number of books.
  - Percentage of books read.
- Save and load the library using `library.txt`.

## How to Run
1. Install Python on your system if it's not already installed.
2. Clone this repository or download the files.
3. Open a terminal/command prompt in the project directory.
4. Run the program using:
   ```bash
   python library_manager.py


Sample Output
Menu
1. Add a book
2. Remove a book
3. Search for a book
4. Display all books
5. Display statistics
6. Exit

Technologies Used
Python (for all functionality)

JSON (for saving and loading the library)