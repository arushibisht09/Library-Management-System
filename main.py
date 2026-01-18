from db import *

while True:
    print("\n===== LIBRARY MANAGEMENT SYSTEM =====")
    print("1. Add Book")
    print("2. Show Books")
    print("3. Add Student")
    print("4. Issue Book")
    print("5. Return Book")
    print("6. Exit")

    choice = int(input("Enter your choice: "))

    if choice == 1:
        book_id = int(input("Book ID: "))
        title = input("Title: ")
        author = input("Author: ")
        year = int(input("Year: "))
        add_book(book_id, title, author, year)
        print("Book added successfully")

    elif choice == 2:
        show_books()

    elif choice == 3:
        student_id = int(input("Student ID: "))
        name = input("Student Name: ")
        student_class = input("Class: ")
        add_student(student_id, name, student_class)
        print("Student added successfully")

    elif choice == 4:
        book_id = int(input("Book ID: "))
        student_id = int(input("Student ID: "))
        issue_book(book_id, student_id)
        print("Book issued successfully")

    elif choice == 5:
        book_id = int(input("Book ID: "))
        student_id = int(input("Student ID: "))
        return_book(book_id, student_id)
        print("Book returned successfully")

    elif choice == 6:
        print("Thank you for using Library Management System")
        break

    else:
        print("Invalid choice")
m