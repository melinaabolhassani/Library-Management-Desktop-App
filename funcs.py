from tkinter import Entry,Button,Label,Frame,IntVar,messagebox,Text
from tkinter.ttk import Combobox,Radiobutton,Checkbutton,Treeview,Scrollbar
from tkcalendar import DateEntry
from dbconnect import connect_db
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
from matplotlib.figure import Figure


def clear_button(parent,check_vars):
    for w in parent.winfo_children():
        if isinstance(w, Combobox):
            w.set("")
        elif isinstance(w, Entry):
            w.delete(0, "end")

        elif isinstance(w, Text):
            w.delete("1.0", "end")

        elif isinstance(w, DateEntry):
            w.set_date(None)
            
    for var in check_vars:
        var.set(0)    

## book
def get_books():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT * FROM books")
    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books

def delete_book(book_id):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM books
            WHERE bookid = ?
        """, (book_id,))

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()

def add_book(name, author, language, category,
             quantity, publishyear, description):
    
    quantity = int(quantity)
    publishyear = int(publishyear)
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "{CALL sp_AddBook (?, ?, ?, ?, ?, ?, ?)}",
            (name, author, language, category,
            quantity, publishyear, description)
        )
        conn.commit()
        messagebox.showinfo("Success",f'book{name}added successfully!')
    except Exception as e:
        print(e)
    finally:    
        cursor.close()
        conn.close()  
           
##member           
def get_members():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""select memberid,firstname,lastname,gender,nationalid,phonenumber,
datediff(year,birthdate,getdate())
,[address],registerdate
from members""")
    members = cursor.fetchall()

    cursor.close()
    conn.close()

    return members

def delete_member(member_id):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            DELETE FROM members
            WHERE memberid = ?
        """, (member_id,))

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()
 
def add_member(firstname, lastname,rd, nationalid,
               phonenumber,birthdate, address):
    
    nationalid= int(nationalid)
    phonenumber = int(phonenumber)
    if rd==1:
        gender='male'
    else:  
        gender='female'
    
    conn = connect_db()
    cursor = conn.cursor()
    try:
        cursor.execute(
            "{CALL sp_Addmember (?, ?, ?, ?, ?, ?, ?)}",
            (firstname, lastname, gender, nationalid,
            phonenumber, birthdate, address)
        )
        conn.commit()
        
        messagebox.showinfo("Success",f'Member{firstname} {lastname} added successfully!')
       
    except Exception as e:
        print(e)
    finally:    
        cursor.close()
        conn.close()    
    
def get_member_by_id(member_id):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT firstname, lastname, gender,
                   nationalid, phonenumber, birthdate, address
            FROM members
            WHERE memberid = ?
        """, (member_id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()            
 
def update_member(member_id, firstname, lastname, gender,
                  nationalid, phone, birthdate, address):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE members
            SET firstname = ?,
                lastname = ?,
                gender = ?,
                nationalid = ?,
                phonenumber = ?,
                birthdate = ?,
                address = ?
            WHERE memberid = ?
        """, (firstname, lastname, gender, nationalid,
              phone, birthdate, address, member_id))

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()  
        
def search_members(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    search = f"%{keyword}%"

    cursor.execute("""
        SELECT memberid, firstname, lastname, gender,
               nationalid, phonenumber, birthdate, address
        FROM members
        WHERE CAST(memberid AS NVARCHAR(20)) LIKE ?
           OR firstname LIKE ?
           OR lastname LIKE ?
           OR CONCAT(firstname, ' ', lastname) LIKE ?
    """, (search, search, search, search))

    members = cursor.fetchall()

    cursor.close()
    conn.close()

    return members       
  
                  
## borrow           

def borrow_search_member(search_value):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT memberid, firstname, lastname
        FROM members
        WHERE firstname + ' ' + lastname LIKE ?
        OR CAST(memberid AS VARCHAR) LIKE ?
    """, ('%' + search_value + '%', '%' + search_value + '%'))

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def borrow_search_book(search_value):

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT bookid, name
        FROM books
        WHERE name LIKE ?
        OR CAST(bookid AS VARCHAR) LIKE ?
    """, ('%' + search_value + '%', '%' + search_value + '%'))

    result = cursor.fetchall()

    cursor.close()
    conn.close()

    return result

def save_borrow(member_id, book_id):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        # Check book availability
        cursor.execute("""
            UPDATE books
            SET quantity = quantity - 1
            WHERE bookid = ? AND quantity > 0
        """, (book_id,))

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        # Save borrowing record
        cursor.execute("""
            INSERT INTO borrowings (bookid, memberid)
            VALUES (?, ?)
        """, (book_id, member_id))

        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()
 
def get_book_by_id(book_id):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            SELECT [name], author, [language], category,
                   quantity, publishyear, [description]
            FROM books
            WHERE bookid = ?
        """, (book_id,))

        return cursor.fetchone()

    finally:
        cursor.close()
        conn.close()        
 
def update_book(book_id, name, author, language, category,
                quantity, publishyear, description):

    conn = connect_db()
    cursor = conn.cursor()

    try:
        cursor.execute("""
            UPDATE books
            SET [name] = ?,
                author = ?,
                [language] = ?,
                category = ?,
                quantity = ?,
                publishyear = ?,
                [description] = ?
            WHERE bookid = ?
        """, (name, author, language, category,
              quantity, publishyear, description, book_id))

        if cursor.rowcount == 0:
            conn.rollback()
            return False

        conn.commit()
        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()        

def search_books(keyword):

    conn = connect_db()
    cursor = conn.cursor()

    search = f"%{keyword}%"

    cursor.execute("""
        SELECT bookid, name, author, language, category,
               quantity, publishyear, [description]
        FROM books
        WHERE CAST(bookid AS NVARCHAR(20)) LIKE ?
           OR name LIKE ?
    """, (search, search))

    books = cursor.fetchall()

    cursor.close()
    conn.close()

    return books
        
        
def search_active_borrowings(search_text):

    conn = connect_db()
    cursor = conn.cursor()

    search_value = '%' + search_text + '%'

    cursor.execute("""
    SELECT
        b.borrowingid,
        m.memberid,
        m.firstname + ' ' + m.lastname,
        bk.bookid,
        bk.name,
        b.borrowingdate
        FROM borrowings b
        JOIN members m ON b.memberid = m.memberid
        JOIN books bk ON b.bookid = bk.bookid
        WHERE b.returndate IS NULL
        AND (
            m.firstname + ' ' + m.lastname LIKE ?
            OR CAST(m.memberid AS NVARCHAR(20)) LIKE ?
            OR bk.name LIKE ?
            OR CAST(bk.bookid AS NVARCHAR(20)) LIKE ?
        )
        ORDER BY b.borrowingdate DESC
    """, (
        search_value,
        search_value,
        search_value,
        search_value
    ))

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def return_book(borrowing_id):

    conn = connect_db()
    cursor = conn.cursor()

    try:

        cursor.execute("""
            UPDATE borrowings
            SET returndate = GETDATE()
            OUTPUT INSERTED.bookid
            WHERE borrowingid = ?
            AND returndate IS NULL
        """, (borrowing_id,))

        result = cursor.fetchone()

        if result is None:
            conn.rollback()
            return False

        book_id = result[0]

        cursor.execute("""
            UPDATE books
            SET quantity = ISNULL(quantity, 0) + 1
            WHERE bookid = ?
        """, (book_id,))

        conn.commit()

        return True

    except Exception:
        conn.rollback()
        raise

    finally:
        cursor.close()
        conn.close()

##dashboard

def member_count():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM members")
    count = cursor.fetchone()[0]

    conn.close()
    return count        

def book_count():
    conn = connect_db()
    cursor = conn.cursor()
    
    cursor.execute("""select sum(quantity) from books""")
    count = cursor.fetchone()[0]

    conn.close()
    return count if count is not None else 0
    
def borrow_count():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("SELECT COUNT(*) FROM borrowings WHERE returndate IS NULL")
    count = cursor.fetchone()[0]

    conn.close()
    return count    

def get_active_borrowings():
    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT
            b.borrowingid,
            m.memberid,
            m.firstname + ' ' + m.lastname,
            bk.bookid,
            bk.name,
            b.borrowingdate
        FROM borrowings b
        JOIN members m ON b.memberid = m.memberid
        JOIN books bk ON b.bookid = bk.bookid
        WHERE b.returndate IS NULL
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    return rows


def show_category_chart():

    conn = connect_db()
    cursor = conn.cursor()

    cursor.execute("""
        SELECT category, quantity
        FROM books
    """)

    rows = cursor.fetchall()

    cursor.close()
    conn.close()

    df = pd.DataFrame.from_records(
        rows,
        columns=["category", "quantity"]
    )

    df["category"] = df["category"].fillna("Uncategorized")

    category_data = (
        df.groupby("category")["quantity"]
        .sum()
        .sort_values(ascending=False)
    )

    fig = Figure(figsize=(4.5,4.5), dpi=100)
    ax = fig.add_subplot(111)

    books = category_data.index.tolist()
    counts = category_data.values.tolist()

    colors = ["#A78BFA", "#60A5FA", "#34D399", "#FBBF24"]

    ax.barh(
        books,
        counts,
        height=0.4,
        color=colors[:len(books)]
    )

    fig.set_facecolor("white")
    ax.set_facecolor("white")

    ax.spines["top"].set_visible(False)
    ax.spines["right"].set_visible(False)

    ax.invert_yaxis()

    fig.subplots_adjust(
        right=0.95,
        bottom=0.12,
        left=0.25,
        top=0.88
    )

    return fig