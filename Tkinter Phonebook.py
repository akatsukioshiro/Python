import Tkinter
from Tkinter import *
import tkMessageBox

def add_func():
    #Function to add names & numbers to phonebook
    #tkMessageBox.showinfo("Test","Content")
    f=open("phonebook.txt","a+")
    add1=E1.get()
    add2=E2.get()
    f.write(add1+" : "+add2+"\n")
    f.close()
    lb.insert(END,add1+" : "+add2)
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    #print(add)
def update_func():
    #FFunction to update those existing numbers/names
    #tkMessageBox.showinfo("Test","Content")
    f = open("phonebook.txt","r")
    lines = f.readlines()
    f.close()
    f = open("phonebook.txt","w+")
    add1=E1.get()
    add2=E2.get()
    selection = lb.curselection()
    #print "lb: ", dir(lb)
    #print lb.get(selection[0])
    #print(selection[0])
    #sel=lb.get(first,last=None)
    sel=lb.get(selection[0])+"\n"
    put=add1+" : "+add2+"\n"
    for line in lines:
        #print(line)
        if line!=sel:
            #print("hi")
            f.write(line)
        else :
            #print("bye")
            f.write(put)
    #print(sel)
    #print(put)
    lb.delete(selection[0])
    lb.insert(selection[0],add1+" : "+add2)
    f.close()
    E1.delete(0, 'end')
    E2.delete(0, 'end')
    
    
def delete_func():
    #Function to delete contacts from phonebook
    #tkMessageBox.showinfo("Test","Content")
    f = open("phonebook.txt","r")
    lines = f.readlines()
    f.close()
    f = open("phonebook.txt","w+")
    selection = lb.curselection()
    sel=lb.get(selection[0])+"\n"
    for line in lines:
        #print(line)
        if line!=sel:
            #print("hi")
            f.write(line)
    #print(sel)
    #print(put)
    lb.delete(selection[0])
    f.close()
    E1.delete(0, 'end')
    E2.delete(0, 'end')
def load_func():
    #All numbers are stored in files, this helps to load phonebook.txt 
    #tkMessageBox.showinfo("Test","Content")
    f = open("phonebook.txt","r")
    lines = f.readlines()
    f.close()
    for line in lines:
        #print(line)
        lb.insert(END,line.strip("\n"))
        
    

root=Tk()
root.title("Phone Book ~ akatsuki")

#Frames of the application
f1=Frame(root)
f1.pack(padx=10, pady=5)
f2=Frame(root)
f2.pack(padx=10, pady=5)
f3=Frame(root)
f3.pack(padx=5, pady=10)
f4=Frame(root)
f4.pack(padx=10, pady=10)

#App size/boundary
root.geometry('{}x{}'.format(250,200))
root.resizable(width=False,height=False)

#Defining and Placing all labels, entry boxes, buttons, list box, scroll bar
L1=Label(f1, text="   Name :  ")
L1.pack(side=LEFT,padx=2.5)
E1=Entry(f1,width=25)
E1.pack(side=LEFT)
L2=Label(f2, text="  Phone :  ")
L2.pack(side=LEFT,padx=2.5)
E2=Entry(f2,width=25)
E2.pack(side=LEFT)
B1=Button(f3, text ="Add", command = add_func, width=6)
B1.pack(side=LEFT,padx=3, pady=1)
B2=Button(f3, text ="Update", command = update_func,width=6)
B2.pack(side=LEFT,padx=3, pady=1)
B3=Button(f3, text ="Delete", command = delete_func,width=6)
B3.pack(side=LEFT,padx=3, pady=1)
B4=Button(f3, text ="Load", command = load_func,width=6)
B4.pack(side=LEFT,padx=3, pady=1)
lb = Listbox(f4, height=6,width=35)
lb.pack(side=LEFT)
sb = Scrollbar(f4,orient=VERTICAL)
sb.pack(side=LEFT,fill=Y)
sb.configure(command=lb.yview)
lb.configure(yscrollcommand=sb.set)
lb.curselection()

#End statement
root.mainloop()
