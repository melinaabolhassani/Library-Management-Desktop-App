from os import system
system("cls")

import pages
from tkinter import Tk,Entry,Button,Label,Frame,Menu,Menubutton



root=Tk()
root.title('library system management')
root.state("zoomed")
root.configure()

#-----------------content frame
content_frame = Frame(root, bg="#26374A")
content_frame.place(x=250, y=0, relwidth=1, relheight=1)

#----------------------menu
menubar=Frame(root,bg="#26374A")
menubar.place(x=0, y=0, width=300, height=1000)

Label(menubar,text="library system",font=('arial',16,''),background="white",fg="#26374A",width=25,height=2).place(x=0, y=10)

Button(menubar, text="dashboard",font=('arial',14,''),background='#26374A',fg='white',activebackground="#26374A",activeforeground="white",bd=0,
    command=lambda :pages.show_dashboard(content_frame)).place(x=30, y=100)
bookmenu = Menubutton(menubar, text="books",font=('arial',14,''),background='#26374A',fg='white',direction='right',activebackground="#26374A",activeforeground="white")
bookmenu.place(x=30, y=150)
book_options = Menu(bookmenu, tearoff=0,bg="#26374A",fg="white",activebackground="#26374A",activeforeground="white")
bookmenu.config(menu=book_options)
book_options.add_command(label="book's list",command=lambda: pages.show_all_book(content_frame))
book_options.add_command(label='add book',command=lambda: pages.show_add_book(content_frame))


Frame(menubar, bg="white", height=1, width=260).place(x=10, y=140)

membermenu = Menubutton(menubar, text="members",font=('arial',14,''),background='#26374A',fg='white',direction='right',activebackground="#26374A",activeforeground="white")
membermenu.place(x=30, y=200)
member_option=Menu(membermenu,tearoff=0,bg="#26374A",fg="white",activebackground="#26374A",activeforeground="white")
membermenu.config(menu=member_option)
member_option.add_command(label="member's list",command=lambda: pages.show_all_members(content_frame))
member_option.add_command(label='add member',command=lambda: pages.show_add_member(content_frame))


Frame(menubar, bg="white", height=1, width=260).place(x=10, y=190)

borrowmenu =Menubutton(menubar,text='borrows',font=('arial',14,''),background='#26374A',fg='white',direction='right',activebackground="#26374A",activeforeground="white")
borrowmenu.place(x=30,y=250)

borrow_optin=Menu(borrowmenu,tearoff=0,bg="#26374A",fg="white",activebackground="#26374A",activeforeground="white")
borrowmenu.config(menu=borrow_optin)
borrow_optin.add_command(label='new borrow',command=lambda: pages.show_add_borrow(content_frame))
borrow_optin.add_command(label='return book',command=lambda:pages.show_return_book(content_frame))

Frame(menubar, bg="white", height=1, width=260).place(x=10, y=240)

quick_acces=Label(menubar,text='quick access',font=('arial',16,''),background='#26374A',fg='white')
quick_acces.place(x=80,y=570)

Frame(menubar, bg="white", height=1, width=260).place(x=10, y=620)

Button(menubar,text="Books List",font=('arial',12,''),bg='#F9D7E3',height=2,width=20,command=lambda:pages.show_all_book(content_frame)).place(x=50,y=640)
Button(menubar,text="Members List",font=('arial',12,''),bg='#F9D7E3',height=2,width=20,command=lambda:pages.show_all_members(content_frame)).place(x=50,y=700)
Button(menubar,text="Borrowings List",font=('arial',12,''),bg='#F9D7E3',height=2,width=20,command=lambda:pages.show_return_book(content_frame)).place(x=50,y=760)



def get_position(event):
    print(f"x={event.x}, y={event.y}")

root.bind("<Button-1>", get_position)


pages.show_dashboard(content_frame)
root.mainloop()
