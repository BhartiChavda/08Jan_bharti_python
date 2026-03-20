import tkinter as tk

a = tk.Tk()
a.title("Calculator")
a.geometry("300x350")

# Display
e = tk.Entry(a,font=("Arial",20),justify="right")
e.grid(row=0,column=0,columnspan=4,pady=10)

def click(num):
    e.insert(tk.END,num)

# Row 1
tk.Button(a,text="7",width=5,height=2,command=lambda:click("7")).grid(row=1,column=0)
tk.Button(a,text="8",width=5,height=2,command=lambda:click("8")).grid(row=1,column=1)
tk.Button(a,text="9",width=5,height=2,command=lambda:click("9")).grid(row=1,column=2)
tk.Button(a,text="/",width=5,height=2,command=lambda:click("/")).grid(row=1,column=3)

# Row 2
tk.Button(a,text="4",width=5,height=2,command=lambda:click("4")).grid(row=2,column=0)
tk.Button(a,text="5",width=5,height=2,command=lambda:click("5")).grid(row=2,column=1)
tk.Button(a,text="6",width=5,height=2,command=lambda:click("6")).grid(row=2,column=2)
tk.Button(a,text="*",width=5,height=2,command=lambda:click("*")).grid(row=2,column=3)

# Row 3
tk.Button(a,text="1",width=5,height=2,command=lambda:click("1")).grid(row=3,column=0)
tk.Button(a,text="2",width=5,height=2,command=lambda:click("2")).grid(row=3,column=1)
tk.Button(a,text="3",width=5,height=2,command=lambda:click("3")).grid(row=3,column=2)
tk.Button(a,text="+",width=5,height=2,command=lambda:click("+")).grid(row=3,column=3)

# Row 4
tk.Button(a,text="0",width=5,height=2,command=lambda:click("0")).grid(row=4,column=0)
tk.Button(a,text=".",width=5,height=2,command=lambda:click(".")).grid(row=4,column=1)

# Equal
def equal():
    result = eval(e.get())
    e.delete(0,tk.END)
    e.insert(0,result)

tk.Button(a,text="=",width=11,height=2,command=equal).grid(row=4,column=2,columnspan=2)

a.mainloop()