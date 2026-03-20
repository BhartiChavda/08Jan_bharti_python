import tkinter
from tkinter import ttk
from tkinter import messagebox

a=tkinter.Tk()
a.title("demo")
a.geometry("400x500")
a.config(background="skyblue")

l1=tkinter.Label(a,text="first name",bg="skyblue",fg="white",font="Corbel 16 bold")
l1.grid(row=0,column=0,sticky="w")
l2=tkinter.Label(a,text="last name",bg="skyblue",fg="white",font="Corbel 16 bold")
l2.grid(row=1,column=0,sticky="w")

t1=tkinter.Entry(a)
t1.grid(row=0,column=1,sticky="w")
t2=tkinter.Entry(a)
t2.grid(row=1,column=1,sticky="w")

m=tkinter.Radiobutton(value=0, text="male",bg="skyblue",fg="white",font="Corbel 16 bold")
m.grid(row=2,column=0,sticky="w")
f=tkinter.Radiobutton(value=1, text="female",bg="skyblue",fg="white",font="Corbel 16 bold")
f.grid(row=2,column=1,sticky="w")

city=['rajkot','surat','haripar']
cty=ttk.Combobox(value=city)
cty.grid(row=3,column=0,sticky="w")
def btnclick():
    print("button clicked")
    print(f"first name:{t1.get()}")
    print(f"last name:{t2.get()}")

    messagebox.showinfo("Success","Form Submitted Successfully")

btn=tkinter.Button(a,text="submit",bg="green",fg="white",font="Corbel 16 bold",command=btnclick)
btn.grid(row=6,column=1,sticky="w")







a.mainloop()
