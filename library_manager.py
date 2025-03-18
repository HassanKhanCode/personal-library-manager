import json  # For saving and loading the library

# Show the menu options
def display_menu():
    print("\nPersonal Library Manager")
    print("1. Add a book")
    print("2. Remove a book")
    print("3. Search for a book")
    print("4. Display all books")
    print("5. Show statistics")
    print("6. Exit")

# Add a book to the library
def add_book(library):
    title = input("Title: ").strip()
    author = input("Author: ").strip()
    year = input("Year: ").strip()
    genre = input("Genre: ").strip()
    read = input("Read (yes/no): ").strip().lower() == 'yes'  # Check if the book is read
    library.append({"Title": title, "Author": author, "Year": int(year), "Genre": genre, "Read": read})
    save_library(library)  # Save after adding the book
    print("Book added!")

# Remove a book from the library by its title
def remove_book(library):
    title = input("Title of book to remove: ").strip()
    for book in library:
        if book["Title"].lower() == title.lower():  # Case-insensitive match
            library.remove(book)
            print("Book removed!")
            return
    print("Book not found.")

# Search for books by title or author
def search_book(library):
    query = input("Search by title or author: ").strip().lower()
    results = [book for book in library if query in book["Title"].lower() or query in book["Author"].lower()]
    for book in results:
        # Show matching books
        print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")
    if not results:
        print("No books found.")

# Display all books in the library
def display_books(library):
    if not library:  # Check if library is empty
        print("Library is empty.")
    for book in library:
        # Show each book in a formatted way
        print(f"{book['Title']} by {book['Author']} ({book['Year']}) - {book['Genre']} - {'Read' if book['Read'] else 'Unread'}")

# Show total books and percentage of read books
def show_statistics(library):
    total = len(library)
    read = sum(1 for book in library if book["Read"])
    # Print statistics
    print(f"Total books: {total}")
    print(f"Books read: {read} ({(read / total * 100):.2f}%)" if total > 0 else "No books to show statistics.")

# Save the library to a file
def save_library(library):
    with open("library.txt", "w") as f:
        json.dump(library, f, indent=4)  # Add indent=4 for better readability
    print("Library saved!")

# Load the library from a file
def load_library():
    try:
        with open("library.txt", "r") as f:
            return json.load(f)  # Load library data from file
    except FileNotFoundError:  # If file doesn't exist, return empty library
        return []

# Main function to run the program
def main():
    library = load_library()  # Load existing library or start fresh
    while True:
        display_menu()  # Show the menu options
        choice = input("Choose an option: ").strip()
        if choice == '1':  # Add a book
            add_book(library)
        elif choice == '2':  # Remove a book
            remove_book(library)
        elif choice == '3':  # Search for books
            search_book(library)
        elif choice == '4':  # Display all books
            display_books(library)
        elif choice == '5':  # Show statistics
            show_statistics(library)
        elif choice == '6':  # Save and exit
            save_library(library)
            print("Goodbye!")
            break
        else:
            print("Invalid choice!")  # Handle invalid input

# Run the program
if __name__ == "__main__":
    main()
