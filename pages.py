from tkinter import Entry,Button,Label,Frame,IntVar,messagebox,Text,LabelFrame,Toplevel
from tkinter.ttk import Combobox,Radiobutton,Checkbutton,Treeview,Scrollbar
from tkcalendar import DateEntry
from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg
import funcs


def show_dashboard(content_frame):
        
    for widget in content_frame.winfo_children():
        widget.destroy()
        
    dashboard_frame = Frame(content_frame, bg='#F2F4F7')
    dashboard_frame.place(x=0,y=0,relwidth=1,relheight=1)

    Label(dashboard_frame,text='Library dashboard', font=('arial',18,''), fg='black', background='#F2F4F7').place(x=150,y=12)

    #vichats
    members_label = Label(dashboard_frame,font=("arial", 12, ""),bg="#F9D7E3",fg="black",height=6,width=35,highlightthickness=3,
    highlightbackground="#D0D0D0",highlightcolor="#D0D0D0")
    members_label.place(x=150, y=90)
    members_label.config(text=f"Total Members\n\n{funcs.member_count()}")
    
    books_label = Label(dashboard_frame,font=("arial", 12, ""),bg="#F9D7E3",fg="black",height=6,width=35,highlightthickness=3,
    highlightbackground="#D0D0D0",highlightcolor="#D0D0D0")
    books_label.place(x=490, y=90)
    books_label.config(text=f"Total Books\n\n{funcs.book_count()}")
    
    borrow_label = Label(dashboard_frame,font=("arial", 12, ""),bg="#F9D7E3",fg="black",height=6,width=35,highlightthickness=3,
    highlightbackground="#D0D0D0",highlightcolor="#D0D0D0")
    borrow_label.place(x=830, y=90)
    borrow_label.config(text=f"Current deposits\n\n{funcs.borrow_count()}")
    
    
    Label(dashboard_frame,text="Active Borrowings",font=("Arial", 16, ''),bg="#F2F4F7").place(x=150, y=250)

    #Treeview
    columns = ("Borrow ID", "Member Name", "Book Name", "Borrow Date")
    #scrollbar
    borrow_scroll = Scrollbar(dashboard_frame)
    borrow_scroll.place(x=650, y=290, height=500)
    
    
    borrow_tree = Treeview(
        dashboard_frame,
        columns=columns,
        show="headings",
        height=10,
        yscrollcommand=borrow_scroll.set
    )

    borrow_scroll.config(command=borrow_tree.yview)
    
 
    for col in columns:
        borrow_tree.heading(col, text=col)

    borrow_tree.column("Borrow ID", width=100, anchor="center")
    borrow_tree.column("Member Name", width=200, anchor="center")
    borrow_tree.column("Book Name", width=200, anchor="center")
    borrow_tree.column("Borrow Date", width=150, anchor="center")


    borrow_tree.place(x=150, y=290, width=500, height=500)

    rows =funcs.get_active_borrowings()

    for row in rows:
        borrow_tree.insert("", "end", values=tuple(row))

    #chrat
    Label(dashboard_frame,text="Books by Quantity",font=("Arial", 16, ''),bg="#F2F4F7").place(x=700, y=250)
    fig = funcs.show_category_chart()

    canvas = FigureCanvasTkAgg(fig, master=dashboard_frame)
    canvas.draw()

    canvas.get_tk_widget().place(x=700,y=300,width=500,height=470)

#----------------
def show_add_member(content_frame):
        
    for widget in content_frame.winfo_children():
        widget.destroy()
        
    add_member_frame = Frame(content_frame, bg='#F2F4F7')
    add_member_frame.place(x=0,y=0,relwidth=1,relheight=1)
    
    
    Label(add_member_frame,text='To add a member, please fill in the fields correctly.',font=('arial',10),bg='#F2F4F7').place(x=200, y=50)

    
    Label(add_member_frame,text='first name:',font=('arial',12),bg='#F2F4F7').place(x=200, y=100)
    member_fname=Entry(add_member_frame,width=20,font=('arial',12))
    member_fname.place(x=350,y=100)
    
    Label(add_member_frame,text='last name:',font=('arial',12),bg='#F2F4F7').place(x=200, y=140)
    member_lname=Entry(add_member_frame,width=20,font=('arial',12))
    member_lname.place(x=350,y=140)
    
    rd = IntVar()
    Label(add_member_frame, text="gender:", bg="#F2F4F7", font=("arial", 12)).place(x=200, y=180)
    Radiobutton(add_member_frame, variable=rd, text="male", value=1).place(x=350, y=180)
    Radiobutton(add_member_frame, variable=rd, text="female", value=2).place(x=450, y=180)
    
    Label(add_member_frame,text='national number:',font=('arial',12),bg='#F2F4F7').place(x=200, y=220)
    national_number=Entry(add_member_frame,width=10,font=('arial',12))
    national_number.place(x=350,y=220)
    Label(add_member_frame,text='*only 10 numbers',font=('arial',8),bg='#F2F4F7',fg='red').place(x=500, y=220)

    
    
    Label(add_member_frame,text='phone number:',font=('arial',12),bg='#F2F4F7').place(x=200, y=260)
    phone_number=Entry(add_member_frame,width=11,font=('arial',12))
    phone_number.place(x=350,y=260)
    Label(add_member_frame,text='*only 11 numbers',font=('arial',8),bg='#F2F4F7',fg='red').place(x=500, y=260)

    
    Label(add_member_frame,text='birthdate:',font=('arial',12),bg='#F2F4F7').place(x=200, y=300)
    birthdate = DateEntry(add_member_frame,font=("arial", 12),width=10,date_pattern="yyyy-mm-dd")
    birthdate.place(x=350,y=300)
    birthdate.delete(0,'end')
    Label(add_member_frame,text='*only for ages over 7',font=('arial',8),bg='#F2F4F7',fg='red').place(x=500, y=300)

    Label(add_member_frame,text='address:',font=('arial',12),bg='#F2F4F7').place(x=200, y=340)
    address=Text(add_member_frame,width=30,height=5,font=('arial',12))
    address.place(x=350,y=340)
  

    Button(add_member_frame,text="clear",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=lambda: funcs.clear_button(add_member_frame, [rd])).place(x=200, y=600)

    Button(add_member_frame,text="save",font=("Arial", 11),bg="#26374A",fg="white",width=10, command= lambda: funcs.add_member(member_fname.get(),member_lname.get(),rd.get(),national_number.get(),phone_number.get(),birthdate.get_date(),address.get("1.0", "end-1c"))).place(x=350, y=600)
  

def show_all_members(content_frame):

    for widget in content_frame.winfo_children():
        widget.destroy()

    all_members_frame = Frame(content_frame, bg="#F2F4F7")
    all_members_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # title
    Label(all_members_frame,text="All Members",font=("Arial", 22, "bold"),bg="#F2F4F7",fg="black").place(x=100, y=25)

    # search box
    search_entry = Entry(all_members_frame,font=("Arial", 12),width=30)
    search_entry.place(x=100, y=85)

    search_entry.insert(0, "Search members...")
    def on_focus_in(event):
        if search_entry.get() == "Search members...":
            search_entry.delete(0, "end")
            search_entry.config(fg="black")


    def on_focus_out(event):
        if search_entry.get().strip() == "":
            search_entry.insert(0, "Search members...")
            search_entry.config(fg="gray")


    search_entry.bind("<FocusIn>", on_focus_in)
    search_entry.bind("<FocusOut>", on_focus_out)
    search_entry.bind("<KeyRelease>", lambda event: search_member())


    #  treeview
    columns = ("ID", "First Name", "Last Name", "gender","National ID","Phone number","age","address","registered date",)

    table = Treeview(all_members_frame,columns=columns,show="headings",height=1)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    table.place(x=100, y=140, width=1120, height=650)

    members = funcs.get_members()

    for member in members:
        table.insert("", "end", values=tuple(member))
        
        
    # scrollbar
    scrollbar = Scrollbar(
        all_members_frame,
        orient="vertical",
        command=table.yview
    )
    scrollbar.place(x=1210, y=140, height=650)

    table.configure(yscrollcommand=scrollbar.set)

    def search_member():

        keyword = search_entry.get().strip()

        # Clear table
        for item in table.get_children():
            table.delete(item)

        # search results
        members = funcs.search_members(keyword)

        # insert table
        for member in members:
            table.insert("", "end", values=tuple(member))
            
        search_entry.bind("<KeyRelease>", lambda event: search_member())    
    
    def delete_selected_member():

        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a member!")
            return

        row = table.item(selected_item[0])["values"]
        member_id = row[0]

        confirm = messagebox.askyesno("Confirm Delete","Are you sure you want to delete this member?")

        if not confirm:
            return

        try:
            result = funcs.delete_member(member_id)

            if result:
                messagebox.showinfo("Success", "Member deleted successfully!")

                table.delete(selected_item[0])

            else:
                messagebox.showwarning("Warning", "Member not found!")

        except Exception as e:
            messagebox.showerror("Error", str(e))
            
            
    def edit_selected_member():

        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a member!")
            return

        row = table.item(selected_item[0])["values"]
        member_id = row[0]

        try:
            member = funcs.get_member_by_id(member_id)

            if member is None:
                messagebox.showwarning("Warning", "Member not found!")
                return

            firstname, lastname, gender, nationalid, phone, birthdate, address = member

            #Toplevel
            edit_window = Toplevel(all_members_frame)
            edit_window.title("Edit Member")
            edit_window.geometry("500x550")
            edit_window.configure(bg="#F2F4F7")
            edit_window.resizable(False, False)

            Label(edit_window, text="First Name:", bg="#F2F4F7").place(x=50, y=90)

            fname_entry = Entry(edit_window, width=30)
            fname_entry.place(x=180, y=90)
            fname_entry.insert(0, firstname or "")

            Label(edit_window, text="Last Name:", bg="#F2F4F7").place(x=50, y=140)

            lname_entry = Entry(edit_window, width=30)
            lname_entry.place(x=180, y=140)
            lname_entry.insert(0, lastname or "")

       
            Label(edit_window, text="Gender:", bg="#F2F4F7").place(x=50, y=190)

            gender_entry = Entry(edit_window, width=30)
            gender_entry.place(x=180, y=190)
            gender_entry.insert(0, gender or "")

            Label(edit_window, text="National ID:", bg="#F2F4F7").place(x=50, y=240)

            nationalid_entry = Entry(edit_window, width=10)
            nationalid_entry.place(x=180, y=240)
            nationalid_entry.insert(0, nationalid or "")


            Label(edit_window, text="Phone:", bg="#F2F4F7").place(x=50, y=290)

            phone_entry = Entry(edit_window, width=11)
            phone_entry.place(x=180, y=290)
            phone_entry.insert(0, phone or "")

            Label(edit_window, text="Birth Date:", bg="#F2F4F7").place(x=50, y=340)

            birthdate_entry = Entry(edit_window, width=30)
            birthdate_entry.place(x=180, y=340)
            birthdate_entry.insert(0, str(birthdate) if birthdate else "")

            Label(edit_window, text="Address:", bg="#F2F4F7").place(x=50, y=390)

            address_entry = Entry(edit_window, width=30)
            address_entry.place(x=180, y=390)
            address_entry.insert(0, address or "")

            def save_changes():

                new_firstname = fname_entry.get().strip()
                new_lastname = lname_entry.get().strip()
                new_gender = gender_entry.get().strip()
                new_nationalid = nationalid_entry.get().strip()
                new_phone = phone_entry.get().strip()
                new_birthdate = birthdate_entry.get().strip()
                new_address = address_entry.get().strip()

                if not new_firstname or not new_lastname:
                    messagebox.showwarning("Warning","First name and last name are required!")
                    return

                try:
                    result = funcs.update_member(
                        member_id,
                        new_firstname,
                        new_lastname,
                        new_gender,
                        new_nationalid,
                        new_phone,
                        new_birthdate,
                        new_address
                    )

                    if result:
                        messagebox.showinfo("Success","Member updated successfully!")

                        #refresh
                        for item in table.get_children():
                            table.delete(item)

                        members = funcs.get_members()

                        for member in members:
                            table.insert("", "end", values=tuple(member))

                        edit_window.destroy()

                    else:
                        messagebox.showwarning("Warning","Member not found!")

                except Exception as e:
                    messagebox.showerror("Error", str(e))

            Button(edit_window,text="Save Changes",font=("Arial", 12, "bold"),bg="#26374A",fg="white",command=save_changes).place(x=180, y=460, width=150, height=40)

        except Exception as e:
            messagebox.showerror("Error", str(e))
        
               
    # buttons

    Button(all_members_frame,text="Edit",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=edit_selected_member).place(x=1015, y=85)

    Button(all_members_frame,text="Delete",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=delete_selected_member).place(x=1130, y=85)    
    

#---------------
def show_add_book(content_frame):
        
    for widget in content_frame.winfo_children():
        widget.destroy()
     
            
    add_book_frame = Frame(content_frame, bg='#F2F4F7')
    add_book_frame.place(x=0,y=0,relwidth=1,relheight=1)
    
    Label(add_book_frame,text='To add a book, please fill in the fields correctly.',font=('arial',10),bg='#F2F4F7').place(x=200, y=50)

    Label(add_book_frame,text="book's name:",font=('arial',12),bg='#F2F4F7').place(x=200, y=100)
    book_name=Entry(add_book_frame,width=20,font=('arial',12))
    book_name.place(x=350,y=100)
    
    Label(add_book_frame,text="author:",font=('arial',12),bg='#F2F4F7').place(x=200, y=140)
    book_author=Entry(add_book_frame,width=20,font=('arial',12))
    book_author.place(x=350,y=140)
    
    ch1 = IntVar(value=0)
    ch2 = IntVar(value=0)
    ch3 = IntVar(value=0)
    ch4 = IntVar(value=0)
    ch5 = IntVar(value=0)
    Label(add_book_frame, text="language:", bg="#F2F4F7", font=("arial", 12, "")).place(x=200, y=180)
    Checkbutton(add_book_frame, variable=ch1, text="English").place(x=350, y=180)
    Checkbutton(add_book_frame, variable=ch2, text="Aracic").place(x=420, y=180)
    Checkbutton(add_book_frame, variable=ch3, text="Persian").place(x=500, y=180)  
    Checkbutton(add_book_frame, variable=ch4, text="German").place(x=580, y=180)  
    Checkbutton(add_book_frame, variable=ch5, text="French").place(x=660, y=180)  
    
    def get_selected_languages():
        languages = []

        if ch1.get():
            languages.append("English")
        if ch2.get():
            languages.append("Arabic")
        if ch3.get():
            languages.append("Persian")
        if ch4.get():
            languages.append("German")
        if ch5.get():
            languages.append("French")

        return ", ".join(languages)

    
    Label(add_book_frame, text="category:", bg="#F2F4F7",font=("arial", 12, "")).place(x=200, y=220)
    category = Combobox(add_book_frame, values=("website", "application", "both"), state="readonly")
    category.place(x=350, y=220)
    
    Label(add_book_frame,text='quantity:',font=('arial',12),bg='#F2F4F7').place(x=200, y=260)
    quantity=Entry(add_book_frame,width=5,font=('arial',12))
    quantity.place(x=350,y=260)

    Label(add_book_frame,text='publish year:',font=('arial',12),bg='#F2F4F7').place(x=200, y=300)
    publish_year = Entry(add_book_frame,font=("arial", 12, ),width=4)
    publish_year.place(x=350,y=300)
    Label(add_book_frame,text='*Only after 1000 AD',font=('arial',8),bg='#F2F4F7',fg='red').place(x=400, y=300)



    Label(add_book_frame,text='description:',font=('arial',12),bg='#F2F4F7').place(x=200, y=340)
    description=Text(add_book_frame,width=40,height=7,font=('arial',12))
    description.place(x=350,y=340)
    
    #buttons
    Button(add_book_frame,text="clear",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=lambda: funcs.clear_button(add_book_frame, [ch1,ch2,ch4,ch5])).place(x=200, y=600)

    Button(add_book_frame,text="save",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=lambda: funcs.add_book(book_name.get(),book_author.get(),get_selected_languages(),category.get(),quantity.get(),publish_year.get(),description.get("1.0", "end-1c"))).place(x=350, y=600)

 
def show_all_book(content_frame):
    
    for widget in content_frame.winfo_children():
     widget.destroy()

    all_books_frame = Frame(content_frame, bg="#F2F4F7")
    all_books_frame.place(x=0, y=0, relwidth=1, relheight=1)

    # title 
    Label(all_books_frame,text="All books",font=("Arial", 22, "bold"),bg="#F2F4F7",fg="black").place(x=100, y=25)

    # search box
    search_entry = Entry(all_books_frame,font=("Arial", 12),width=30)
    search_entry.place(x=100, y=85)

    search_entry.insert(0, "Search books...")
    
    def on_focus_in(event):
        if search_entry.get() == "Search books...":
            search_entry.delete(0, "end")
            search_entry.config(fg="black")


    def on_focus_out(event):
        if search_entry.get().strip() == "":
            search_entry.insert(0, "Search books...")
            search_entry.config(fg="gray")


    search_entry.bind("<FocusIn>", on_focus_in)
    search_entry.bind("<FocusOut>", on_focus_out)
    search_entry.bind("<KeyRelease>", lambda event: search_book())


    #  treeview
    columns = ("ID", "Name", "author","language", "category","quantity","publish year")

    table = Treeview(all_books_frame,columns=columns,show="headings",height=1)

    for col in columns:
        table.heading(col, text=col)
        table.column(col, width=100, anchor="center")

    table.place(x=100, y=140, width=1120, height=650)


    #   scrollbar
    scrollbar = Scrollbar(
        all_books_frame,
        orient="vertical",
        command=table.yview
    )
    scrollbar.place(x=1210, y=140, height=650)

    table.configure(yscrollcommand=scrollbar.set)
    

    books = funcs.get_books()

    for book in books:
        table.insert("", "end", values=tuple(book))
    
    
    def search_book():

        keyword = search_entry.get().strip()

        # treeview
        for item in table.get_children():
            table.delete(item)

        # get results
        books = funcs.search_books(keyword)

        # insert
        for book in books:
            table.insert("", "end", values=tuple(book))
            
          
        
    def delete_selected_book():

        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a book!")
            return

        row = table.item(selected_item[0])["values"]
        book_id = row[0]

        confirm = messagebox.askyesno("Confirm Delete","Are you sure you want to delete this book?")

        if not confirm:
            return

        try:
            result = funcs.delete_book(book_id)

            if result:
                messagebox.showinfo("Success", "book deleted successfully!")

                table.delete(selected_item[0])

            else:
                messagebox.showwarning("Warning", "book not found!")

        except Exception as e:
            
            messagebox.showerror("Error", str(e))
            
        
    def edit_selected_book():

        selected_item = table.selection()

        if not selected_item:
            messagebox.showwarning("Warning", "Please select a book!")
            return

        row = table.item(selected_item[0])["values"]
        book_id = row[0]

        try:
            book = funcs.get_book_by_id(book_id)

            if book is None:
                messagebox.showwarning("Warning", "Book not found!")
                return

            name, author, language, category, quantity, publishyear, description = book

            # treeviw
            edit_window = Toplevel(all_books_frame)
            edit_window.title("Edit Book")
            edit_window.geometry("550x600")
            edit_window.configure(bg="#F2F4F7")
            edit_window.resizable(False, False)


            Label(edit_window, text="Book Name:", bg="#F2F4F7").place(x=50, y=50)

            name_entry = Entry(edit_window, width=35)
            name_entry.place(x=180, y=50)
            name_entry.insert(0, name or "")

            Label(edit_window, text="Author:", bg="#F2F4F7").place(x=50, y=100)

            author_entry = Entry(edit_window, width=35)
            author_entry.place(x=180, y=100)
            author_entry.insert(0, author or "")

            Label(edit_window, text="Language:", bg="#F2F4F7").place(x=50, y=150)

            language_entry = Entry(edit_window, width=35)
            language_entry.place(x=180, y=150)
            language_entry.insert(0, language or "")

            Label(edit_window, text="Category:", bg="#F2F4F7").place(x=50, y=200)

            category_entry = Entry(edit_window, width=35)
            category_entry.place(x=180, y=200)
            category_entry.insert(0, category or "")

            Label(edit_window, text="Quantity:", bg="#F2F4F7").place(x=50, y=250)

            quantity_entry = Entry(edit_window, width=20)
            quantity_entry.place(x=180, y=250)
            quantity_entry.insert(0, str(quantity) if quantity is not None else "")

            Label(edit_window, text="Publish Year:", bg="#F2F4F7").place(x=50, y=300)

            year_entry = Entry(edit_window, width=4)
            year_entry.place(x=180, y=300)
            year_entry.insert(0, str(publishyear) if publishyear is not None else "")

            Label(edit_window, text="Description:", bg="#F2F4F7").place(x=50, y=350)

            description_entry = Text(edit_window, width=40, height=5)
            description_entry.place(x=180, y=350)

            description_entry.insert("1.0", description or "")

            def save_changes():

                new_name = name_entry.get().strip()
                new_author = author_entry.get().strip()
                new_language = language_entry.get().strip()
                new_category = category_entry.get().strip()
                new_quantity = quantity_entry.get().strip()
                new_year = year_entry.get().strip()
                new_description = description_entry.get("1.0", "end-1c").strip()

                if not new_name:
                    messagebox.showwarning("Warning","Book name is required!")
                    return

                try:
                    if not new_quantity.isdigit() or not new_year.isdigit():
                        messagebox.showwarning("Warning","Quantity and publish year must be numbers!")
                        return

                    result = funcs.update_book(
                        book_id,
                        new_name,
                        new_author,
                        new_language,
                        new_category,
                        int(new_quantity),
                        int(new_year),
                        new_description
                    )

                    if result:
                        messagebox.showinfo("Success","Book updated successfully!")

                        # Refresh table
                        for item in table.get_children():
                            table.delete(item)

                        books = funcs.get_books()

                        for book in books:
                            table.insert("", "end", values=tuple(book))

                        edit_window.destroy()

                    else:
                        messagebox.showwarning("Warning","Book not found!")

                except Exception as e:
                    messagebox.showerror("Error", str(e))

            Button(edit_window,text="Save Changes",font=("Arial", 12, "bold"),bg="#26374A",
                fg="white",command=save_changes).place(x=200, y=520, width=150, height=40)

        except Exception as e:
            messagebox.showerror("Error", str(e))
                    
    # buttons

    Button(all_books_frame,text="Edit",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=edit_selected_book).place(x=1015, y=85)

    Button(all_books_frame,text="Delete",font=("Arial", 11),bg="#26374A",fg="white",width=10,command=delete_selected_book).place(x=1130, y=85)    
    

def show_add_borrow(content_frame):

    for widget in content_frame.winfo_children():
        widget.destroy()

    add_borrow_frame = Frame(content_frame, bg="#F2F4F7")
    add_borrow_frame.place(x=0, y=0, relwidth=1, relheight=1)


    member_id = None
    book_id = None

    # --------------member

    member_frame = LabelFrame(add_borrow_frame,text="Member Information",font=("Arial", 12),bg="#F9D7E3")
    member_frame.place(x=100, y=50, width=500, height=400)

    Label(member_frame,text="Search by name or ID:",bg="white",font=("Arial", 11)).place(x=20, y=35)

    member_search = Entry(member_frame, width=25, font=("Arial", 11))
    member_search.place(x=200, y=35)
    

    #treeview
    member_tree = Treeview(
        member_frame,
        columns=("ID", "Name"),
        show="headings",
        height=8
    )

    member_tree.heading("ID", text="Member ID")
    member_tree.heading("Name", text="Full Name")

    member_tree.column("ID", width=100, anchor="center")
    member_tree.column("Name", width=250, anchor="center")

    member_tree.place(x=20, y=100, width=440, height=180)

    # select member
    Label(member_frame,text="Selected Member:",bg="white").place(x=20, y=300)

    selected_member = Entry(member_frame, width=35, state="readonly")
    selected_member.place(x=150, y=300)

    # Search member
    def find_member():

        nonlocal member_id

        member_id = None
        selected_member.config(state="normal")
        selected_member.delete(0, "end")
        selected_member.config(state="readonly")

        for item in member_tree.get_children():
            member_tree.delete(item)

        search_value = member_search.get().strip()

        if not search_value:
            messagebox.showwarning("Warning", "Enter member name or ID!")
            return

        result = funcs.borrow_search_member(search_value)

        if result:

            for row in result:
                member_tree.insert(
                    "",
                    "end",
                    values=(row[0], f"{row[1]} {row[2]}")
                )

        else:
            messagebox.showinfo("Not Found", "No member found!")

    Button(member_frame,text="Search",command=find_member).place(x=400, y=33)

    def select_member(event):

        nonlocal member_id

        selected_item = member_tree.selection()

        if selected_item:

            row = member_tree.item(selected_item[0], "values")

            member_id = row[0]

            selected_member.config(state="normal")
            selected_member.delete(0, "end")
            selected_member.insert(0, f"{row[0]} - {row[1]}")
            selected_member.config(state="readonly")

    member_tree.bind("<<TreeviewSelect>>", select_member)


    #------------book

    book_frame = LabelFrame(
        add_borrow_frame,
        text="Book Information",
        font=("Arial", 12),
        bg="#F9D7E3"
    )
    book_frame.place(x=650, y=50, width=500, height=400)

    Label(book_frame,text="Search by name or ID:",bg="white",font=("Arial", 11)).place(x=20, y=35)

    book_search = Entry(book_frame, width=25, font=("Arial", 11))
    book_search.place(x=200, y=35)

    # treeview
    book_tree = Treeview(
        book_frame,
        columns=("ID", "Title"),
        show="headings",
        height=8
    )

    book_tree.heading("ID", text="Book ID")
    book_tree.heading("Title", text="Book Name")

    book_tree.column("ID", width=100, anchor="center")
    book_tree.column("Title", width=250, anchor="center")

    book_tree.place(x=20, y=100, width=440, height=180)

    # select book
    Label(book_frame,text="Selected Book:",bg="white").place(x=20, y=300)

    selected_book = Entry(book_frame, width=35, state="readonly")
    selected_book.place(x=150, y=300)

    # Search book
    def find_book():

        nonlocal book_id

        book_id = None
        selected_book.config(state="normal")
        selected_book.delete(0, "end")
        selected_book.config(state="readonly")

        for item in book_tree.get_children():
            book_tree.delete(item)

        search_value = book_search.get().strip()

        if not search_value:
            messagebox.showwarning("Warning", "Enter book name or ID!")
            return

        result = funcs.borrow_search_book(search_value)

        if result:

            for row in result:
                book_tree.insert(
                    "",
                    "end",
                    values=(row[0], row[1])
                )

        else:
            messagebox.showinfo("Not Found", "No book found!")

    Button(book_frame,text="Search",command=find_book).place(x=400, y=33)

    def select_book(event):

        nonlocal book_id

        selected_item = book_tree.selection()

        if selected_item:

            row = book_tree.item(selected_item[0], "values")

            book_id = row[0]

            selected_book.config(state="normal")
            selected_book.delete(0, "end")
            selected_book.insert(0, f"{row[0]} - {row[1]}")
            selected_book.config(state="readonly")

    book_tree.bind("<<TreeviewSelect>>", select_book)

    def save_borrow_record():

        nonlocal member_id, book_id

        if member_id is None:
            messagebox.showwarning("Warning", "Please select a member!")
            return

        if book_id is None:
            messagebox.showwarning("Warning", "Please select a book!")
            return

        try:
            result = funcs.save_borrow(member_id, book_id)

            if result:
                messagebox.showinfo("Success", "Borrowing saved successfully!")

                member_id = None
                book_id = None

                selected_member.config(state="normal")
                selected_member.delete(0, "end")
                selected_member.config(state="readonly")

                selected_book.config(state="normal")
                selected_book.delete(0, "end")
                selected_book.config(state="readonly")

            else:
                messagebox.showwarning("Unavailable", "This book is not available!")

        except Exception as e:
            messagebox.showerror("Error", str(e))


    Button(add_borrow_frame,text="Save Borrow",font=("Arial", 12, "bold"),bg="#26374A",
        fg="white",command=save_borrow_record).place(x=800, y=550, width=180, height=45)
    
    Label(add_borrow_frame,text="To borrow a book,\nPlease search for and select the member's name from the Members frame.\nThen select the desired book from the Books fram(provided it is available)\nThen click the Save borrow button.",justify="left",font=('arial',10),bg='#F2F4F7').place(x=100, y=550)
    
    
    
def show_return_book(content_frame):

    for widget in content_frame.winfo_children():
        widget.destroy()

    return_frame = Frame(content_frame,bg="#F2F4F7")
    return_frame.place(x=0, y=0, relwidth=1, relheight=1)


    # title
    Label(return_frame,text="Return Book",font=("Arial", 22, "bold"),
          bg="#F2F4F7",fg="#030303").place(x=100, y=25)
  

    Label(return_frame,text="Search Borrowing:",font=("Arial", 12, "bold"),
         bg="#F2F4F7",fg="#26374A").place(x=100, y=150)


    # Search box
    search_entry = Entry(return_frame,font=("Arial", 12),width=35,relief="solid",bd=1)
    search_entry.place(x=270, y=150, height=32)


    def search_borrowings():

        search_text = search_entry.get().strip()

        if search_text:
            rows = funcs.search_active_borrowings(search_text)
        else:
            rows = funcs.get_active_borrowings()

        borrow_tree.delete(*borrow_tree.get_children())

        for row in rows:
            borrow_tree.insert("", "end", values=tuple(row))


    Button(return_frame,text="Search",font=("Arial", 11, "bold"),bg="#26374A",fg="white",
    activebackground="#344F6D",cursor="hand2",
    command=search_borrowings).place(x=600, y=150, width=100, height=35)

    def clear_search():

        search_entry.delete(0, "end")
        search_borrowings()


    Button(return_frame,text="Clear",font=("Arial", 11),bg="#F9D7E3",fg="#26374A",cursor="hand2",
        command=clear_search).place(x=720, y=150, width=80, height=35)


    search_entry.bind(
        "<Return>",
        lambda event: search_borrowings()
    )


    # Table Title
    Label(return_frame,text="Active Borrowings",font=("Arial", 15, "bold"),bg="#F4F6FA",fg="#26374A").place(x=150, y=250)


    # Treeview Columns
    columns = (
        "Borrow ID",
        "Member ID",
        "Member Name",
        "Book ID",
        "Book Name",
        "Borrow Date"
    )


    # Scrollbar
    borrow_scroll = Scrollbar(
        return_frame,
        orient="vertical"
    )
    borrow_scroll.place(
        x=1180,
        y=290,
        height=400
    )


    # treeview
    borrow_tree = Treeview(
        return_frame,
        columns=columns,
        show="headings",
        height=15,
        yscrollcommand=borrow_scroll.set
    )

    borrow_scroll.config(command=borrow_tree.yview)

    for col in columns:
        borrow_tree.heading(col, text=col)


    borrow_tree.column("Borrow ID", width=90, anchor="center")
    borrow_tree.column("Member ID", width=90, anchor="center")
    borrow_tree.column("Member Name", width=180, anchor="center")
    borrow_tree.column("Book ID", width=90, anchor="center")
    borrow_tree.column("Book Name", width=200, anchor="center")
    borrow_tree.column("Borrow Date", width=150, anchor="center")


    borrow_tree.place(x=150,y=290,width=1030,height=400)

    search_borrowings()

    def return_selected_book():

        selected_item = borrow_tree.selection()

        if not selected_item:
            messagebox.showwarning(
                "Warning",
                "Please select a borrowing first!",
                parent=return_frame
            )
            return

        row = borrow_tree.item(selected_item[0])

        borrowing_id = row["values"][0]
        book_name = row["values"][4]

        confirm = messagebox.askyesno("Return Book",f"Are you sure you want to return '{book_name}'?",parent=return_frame)

        if not confirm:
            return

        try:

            result = funcs.return_book(borrowing_id)

            if result:

                borrow_tree.delete(selected_item[0])

                messagebox.showinfo("Success","Book returned successfully!",parent=return_frame)

            else:

                messagebox.showwarning("Warning","This borrowing has already been returned!",parent=return_frame)

                search_borrowings()

        except Exception as e:

            messagebox.showerror("Database Error",str(e),parent=return_frame)


    # rrturn Button
    Button(return_frame,text="Return Book",font=("Arial", 12, "bold"),bg="#26374A",fg="white",activebackground="#344F6D",
        cursor="hand2",command=return_selected_book).place(x=900,y=700,width=150,height=40)    