import tkinter
from tkinter import ttk, messagebox
import os

try:
    b = tkinter.Tk()
    b.title("BlogPost")
    b.config(bg="skyblue")
    b.geometry("500x600") 

    #Name
    lbl1 = tkinter.Label(b, text="Enter your name:", bg="skyblue", fg="black", font=("Bahnschrift", 12, "bold"))
    lbl1.grid(row=0, column=0, sticky="w")
    txt1 = tkinter.Entry(b, width=30)
    txt1.grid(row=0, column=1)

    #Post Title
    lbl2 = tkinter.Label(b, text="Post title:", bg="skyblue", fg="black", font=("Bahnschrift", 12, "bold"))
    lbl2.grid(row=1, column=0, sticky="w")
    txt2 = tkinter.Entry(b, width=30)
    txt2.grid(row=1, column=1)

    #Post Content
    lbl3 = tkinter.Label(b, text="Post content:", bg="skyblue", fg="black", font=("Bahnschrift", 12, "bold"))
    lbl3.grid(row=2, column=0, sticky="nw")
    txt3 = tkinter.Text(b, height=5, width=40)
    txt3.grid(row=2, column=1)

    #Save Button
    btn_save = tkinter.Button(b, text="Save", bg="green", fg="white", font="Bahnschrift 12 bold")
    btn_save.grid(row=3, column=1)

    #Listbox
    lbl_list = tkinter.Label(b, text="Saved Posts:", bg="skyblue", fg="black", font=("Bahnschrift", 12, "bold"))
    lbl_list.grid(row=4, column=0, sticky="w")
    post_list = tkinter.Listbox(b, width=50)
    post_list.grid(row=5, column=0, columnspan=2)

    #Post Content Display
    lbl_display = tkinter.Label(b, text="Post Content:", bg="skyblue", fg="black", font=("Bahnschrift", 12, "bold"))
    lbl_display.grid(row=6, column=0, sticky="w")
    display = tkinter.Text(b, height=10, width=50)
    display.grid(row=7, column=0, columnspan=2)

    #Create folder
    if not os.path.exists("posts"):
        os.makedirs("posts")

    #save post
    def save_post():
        name = txt1.get()
        title = txt2.get()
        content_text = txt3.get("1.0", "end")

        if not name or not title or not content_text:
            messagebox.showwarning("Warning", "Please fill all fields!")
            return

        safe_title = "".join(c for c in title if c.isalnum() or c in (" ", "_")).rstrip()
        filename = f"posts/{safe_title}.txt"

        with open(filename, "w", encoding="utf-8") as f:
            f.write(f"Name: {name}\nTitle: {title}\nContent:\n{content_text}\n")

        messagebox.showinfo("Success", "Post created successfully!")
        txt1.delete(0, "end")
        txt2.delete(0, "end")
        txt3.delete("1.0", "end")
        load_posts()

    btn_save.config(command=save_post)

    # Load Posts
    def load_posts():
        post_list.delete(0, tkinter.END)
        files = os.listdir("posts")
        for f in files:
            post_list.insert(tkinter.END, f)

    # View Post
    def view_post(event):
        try:
            selected = post_list.get(post_list.curselection())
            with open(f"posts/{selected}", "r", encoding="utf-8") as file:
                data = file.read()
            display.delete("1.0", "end")
            display.insert(tkinter.END, data)
        except Exception as e:
            messagebox.showerror("Error", str(e))
    post_list.bind("<<ListboxSelect>>", view_post)

    load_posts()
    b.mainloop()

except Exception as e:
    print("Error:", e)