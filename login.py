import interface
import tkinter as tk
from tkinter import messagebox

root = tk.Tk()
root.title("Login")
root.geometry("400x400")
root.configure(bg="lightblue")

def login():
    username = username_entry.get()
    password = password_entry.get()

    if username == "admin" and password == "1234":
        messagebox.showinfo("Login successful", "Welcome, " + username)
    else:
        messagebox.showerror("Login failed", "Invalid username or password")

    username_entry.delete(0, tk.END)
    password_entry.delete(0, tk.END)

username_label = tk.Label(root, text="Username:", font=("Arial", 12))
username_label.pack()
username_entry = tk.Entry(root, font=("Arial", 12))
username_entry.pack()

password_label = tk.Label(root, text="Password:", font=("Arial", 12))
password_label.pack()
password_entry = tk.Entry(root, show="*", font=("Arial", 12))
password_entry.pack()

login_button = tk.Button(root, text="Login", font=("Arial", 12), command=login)
login_button.pack()

root.mainloop()