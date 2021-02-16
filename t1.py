from tkinter import *
import tkinter.messagebox as tmsg
from main import *
import os


root = Tk()
root.title('AFC_BY_AK-HACKS')
root.minsize(590,500)
root.maxsize(590,500)

def hi():
	if (fromm.get())>(too.get()):
		tmsg.showwarning('Warning',f'You Cannot Make Folders From {(fromm.get())} to {(too.get())}')
	elif (fromm.get())==0 or (too.get())==0:
		tmsg.showwarning('Warning',f'0 Is Not Allowed')
	else:
		en1.config(state=DISABLED)
		en2.config(state=DISABLED)
		b2.config(state=DISABLED)
		b1.config(state=NORMAL)

def decision(tf,msg,txt):
	aa = os.path.exists(f'{(too.get())}')
	if aa==tf:
		tmsg.showinfo('Done',msg)
		b1.config(state=DISABLED,text=txt)
		en1.config(state=NORMAL)
		en2.config(state=NORMAL)
		b2.config(state=NORMAL)
	else:
		pass

def folder(folder):
	if b1['state']==DISABLED:
		pass
	else:
		createfolders((fromm.get()),(too.get()))
		b1.config(text="PLEASE WAIT...")
		decision(True,'All Folders Has Been Created Successfully',"CREATE FOLDERS")

def del_mode():
	b1.config(text="DELETE FOLDER",command=dell)
	b1.bind('<Enter>',dell)
	b3.config(text='CREATE [ MODE ]',command=crt)

def crt():
	b1.config(text="CREATE FOLDER",command=folder)
	b1.bind('<Enter>',folder)
	b3.config(text='DEL [ MODE ]',command=del_mode)

def dell(dell):
	if b1['state']==DISABLED:
		pass
	else:
		deletefolders((fromm.get()),(too.get()))
		decision(False,'All Folders Has Been Deleted Successfully',"DELETE FOLDERS")

Label(text="Automatic Folder Creator",font="comicsansms 14 bold",bg="black",fg="white").pack()

fromm = IntVar()
fromm.set(1)
too = IntVar()
too.set(100)

f1 = Frame(borderwidth=10,bg="black")

Label(f1,text="FROM: ",font="comicsansms 14 bold",bg="black",fg="white").pack(side=LEFT)
en1 = Entry(f1,textvariable=fromm,fg="black",bg="white")
en1.pack(side=LEFT)

Label(f1,text="TO: ",font="comicsansms 14 bold",bg="black",fg="white").pack(side=LEFT)
en2 = Entry(f1,textvariable=too,fg="black",bg="white")
en2.pack(side=LEFT)

Label(f1,text="",font="comicsansms 14 bold",bg="black",fg="white").pack(side=LEFT)
b2 = Button(f1,text="DONE",bg="black",fg="white",font="comicsansms 20 bold",command=hi)
b2.pack(side=LEFT)

Label(f1,text="",font="comicsansms 14 bold",bg="black",fg="white").pack(side=LEFT)
b3 = Button(f1,text="DEL [ MODE ]",bg="black",fg="white",font="comicsansms 7 bold",command=del_mode)
b3.pack(side=LEFT)


f1.pack(anchor="w")

b1 = Button(text="CREATE",bg="black",fg="white",font="comicsansms 20 bold",borderwidth=5,padx=220,pady=170,state=DISABLED,command=folder)
b1.bind('<Enter>',folder)
b1.pack()

root.config(bg="black")
root.mainloop()
