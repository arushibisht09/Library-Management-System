from db_config import get_connection
from datetime import date

# Add book
def add_book(book_id, title, author, year):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO books VALUES (%s,%s,%s,%s,'Available')",
        (book_id, title, author, year)
    )
    conn.commit()
    conn.close()

# Show all books
def show_books():
    conn = get_connection()
    cur = conn.cursor()
    cur.execute("SELECT * FROM books")
    for row in cur.fetchall():
        print(row)
    conn.close()

# Add student
def add_student(student_id, name, student_class):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO students VALUES (%s,%s,%s)",
        (student_id, name, student_class)
    )
    conn.commit()
    conn.close()

# Issue book
def issue_book(book_id, student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "INSERT INTO issue (book_id, student_id, issue_date) VALUES (%s,%s,%s)",
        (book_id, student_id, date.today())
    )
    cur.execute(
        "UPDATE books SET status='Issued' WHERE book_id=%s",
        (book_id,)
    )
    conn.commit()
    conn.close()

# Return book
def return_book(book_id, student_id):
    conn = get_connection()
    cur = conn.cursor()
    cur.execute(
        "UPDATE issue SET return_date=%s WHERE book_id=%s AND student_id=%s",
        (date.today(), book_id, student_id)
    )
    cur.execute(
        "UPDATE books SET status='Available' WHERE book_id=%s",
        (book_id,)
    )
    conn.commit()
    conn.close()
