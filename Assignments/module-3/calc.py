import tkinter as tk

# window create
root = tk.Tk()
root.title("Simple Calculator")
root.geometry("700x800")

# entry box
e = tk.Entry(root, width=20, font=("Arial",20), borderwidth=5)
e.grid(row=0, column=0, columnspan=3, padx=10, pady=10)

# button click function
def click(num):
    current = e.get()
    e.delete(0, tk.END)
    e.insert(0, str(current) + str(num))

# clear function
def clear():
    e.delete(0, tk.END)

# equal function
def equal():
    result = eval(e.get())
    e.delete(0, tk.END)
    e.insert(0, result)

# buttons
b1 = tk.Button(root,text="1",padx=20,pady=20,command=lambda:click(1))
b2 = tk.Button(root,text="2",padx=20,pady=20,command=lambda:click(2))
b3 = tk.Button(root,text="3",padx=20,pady=20,command=lambda:click(3))

b4 = tk.Button(root,text="4",padx=20,pady=20,command=lambda:click(4))
b5 = tk.Button(root,text="5",padx=20,pady=20,command=lambda:click(5))
b6 = tk.Button(root,text="6",padx=20,pady=20,command=lambda:click(6))

b7 = tk.Button(root,text="7",padx=20,pady=20,command=lambda:click(7))
b8 = tk.Button(root,text="8",padx=20,pady=20,command=lambda:click(8))
b9 = tk.Button(root,text="9",padx=20,pady=20,command=lambda:click(9))

b0 = tk.Button(root,text="0",padx=20,pady=20,command=lambda:click(0))

# operators
add = tk.Button(root,text="+",padx=20,pady=20,command=lambda:click("+"))
sub = tk.Button(root,text="-",padx=20,pady=20,command=lambda:click("-"))
mul = tk.Button(root,text="*",padx=20,pady=20,command=lambda:click("*"))
div = tk.Button(root,text="/",padx=20,pady=20,command=lambda:click("/"))

equalbtn = tk.Button(root,text="=",padx=20,pady=20,command=equal)
clearbtn = tk.Button(root,text="C",padx=20,pady=20,command=clear)

# grid
b1.grid(row=3,column=0)
b2.grid(row=3,column=1)
b3.grid(row=3,column=2)

b4.grid(row=2,column=0)
b5.grid(row=2,column=1)
b6.grid(row=2,column=2)

b7.grid(row=1,column=0)
b8.grid(row=1,column=1)
b9.grid(row=1,column=2)

b0.grid(row=4,column=0)

add.grid(row=5,column=0)
sub.grid(row=5,column=1)
mul.grid(row=5,column=2)

div.grid(row=6,column=0)
equalbtn.grid(row=6,column=1)
clearbtn.grid(row=6,column=2)

root.mainloop()