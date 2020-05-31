from tkinter import *
import backend

window = Tk()

window.wm_title("Book Store")

#labels
l1 = Label(window,text='title')
l2 = Label(window,text='Author')
l3 = Label(window,text='Year')
l4 = Label(window,text='ISBN')
l1.grid(row=0,column=0)
l2.grid(row=0,column=2)
l3.grid(row=1,column=0)
l4.grid(row=1,column=2)

#entries
Title_value = StringVar()
Author_value = StringVar()
Year_value = StringVar()
ISBN_value = StringVar()
e1 = Entry(window,textvariable=Title_value)
e2 = Entry(window,textvariable=Author_value)
e3 = Entry(window,textvariable=Year_value)
e4 = Entry(window,textvariable=ISBN_value)
e1.grid(row=0,column=1)
e2.grid(row=0,column=3)
e3.grid(row=1,column=1)
e4.grid(row=1,column=3)

#listbox
lb1 = Listbox(window,height =8,width=35)
lb1.grid(row=2,column=0,rowspan=8,columnspan=2)

#scrollbar
sb = Scrollbar(window)
sb.grid(row=2,column=2,rowspan = 6)

#binding list and scrollbar
lb1.configure(yscrollcommand=sb.set)
sb.configure(command=lb1.yview)

#all functions to call backend
def viewall():
    lb1.delete(0,END)
    for row in backend.view():
        lb1.insert(END,row)

def search_button():
    lb1.delete(0,END)
    for row in backend.search(Title_value.get(),Author_value.get(),Year_value.get(),ISBN_value.get()):
        lb1.insert(END,row)

def Add_entry():
    backend.insert(Title_value.get(),Author_value.get(),Year_value.get(),ISBN_value.get())
    lb1.delete(0,END)
    lb1.insert(END,(Title_value.get(),Author_value.get(),Year_value.get(),ISBN_value.get()))

def get_row(event):
    try:
        global values
        index = lb1.curselection()[0]
        values = lb1.get(index)
        e1.delete(0,END)
        e2.delete(0,END)
        e3.delete(0,END)
        e4.delete(0,END)
        e1.insert(0,values[1])
        e2.insert(0,values[2])
        e3.insert(0,values[3])
        e4.insert(0,values[4])
    except IndexError:
        pass

lb1.bind("<<ListboxSelect>>",get_row)

def delete_comm():
    backend.delete(values[0])

def update_command():
    backend.update(values[0],Title_value.get(),Author_value.get(),Year_value.get(),ISBN_value.get())


#buttons
b1 = Button(window,text='View all',width=20,command=viewall)
b2 = Button(window,text='Search Entry',width=20,command=search_button)
b3 = Button(window,text='Add Entry',width=20,command=Add_entry)
b4 = Button(window,text='Update',width=20,command=update_command)
b5 = Button(window,text='Delete',width=20,command=delete_comm)
b6 = Button(window,text='Close',width=20,command=window.destroy)
b1.grid(row=3,column=3)
b2.grid(row=4,column=3)
b3.grid(row=5,column=3)
b4.grid(row=6,column=3)
b5.grid(row=7,column=3)
b6.grid(row=8,column=3)



window.mainloop()