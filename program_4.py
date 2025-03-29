#Programmer: Timothy Pickering
#Date: 3/28/2025
#Title: Phonebook database interface

#Required module
import tkinter as tk
from tkinter import messagebox
import sqlite3

#Function to initialize the database
def init_db():
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute('''CREATE TABLE IF NOT EXISTS Entries (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    phone TEXT NOT NULL)''')
    conn.commit()
    conn.close()

#Function to add a new entry
def add_entry():
    name = name_entry.get()
    phone = phone_entry.get()
    if name and phone:
        conn = sqlite3.connect("phonebook.db")
        cur = conn.cursor()
        cur.execute("INSERT INTO Entries (name, phone) VALUES (?, ?)", (name, phone))
        conn.commit()
        conn.close()
        messagebox.showinfo("Success", "Entry added successfully!")
        name_entry.delete(0, tk.END)
        phone_entry.delete(0, tk.END)
    else:
        messagebox.showerror("Error", "Please enter both name and phone number.")

#Function to lookup a phone number
def lookup_entry():
    name = name_entry.get()
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("SELECT phone FROM Entries WHERE name = ?", (name,))
    result = cur.fetchone()
    conn.close()
    if result:
        messagebox.showinfo("Phone Number", f"{name}: {result[0]}")
    else:
        messagebox.showerror("Error", "Entry not found.")

#Function to update a phone number
def update_entry():
    name = name_entry.get()
    phone = phone_entry.get()
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("UPDATE Entries SET phone = ? WHERE name = ?", (phone, name))
    conn.commit()
    conn.close()
    if cur.rowcount:
        messagebox.showinfo("Success", "Phone number updated successfully!")
    else:
        messagebox.showerror("Error", "Entry not found.")

#Function to delete an entry
def delete_entry():
    name = name_entry.get()
    conn = sqlite3.connect("phonebook.db")
    cur = conn.cursor()
    cur.execute("DELETE FROM Entries WHERE name = ?", (name,))
    conn.commit()
    conn.close()
    if cur.rowcount:
        messagebox.showinfo("Success", "Entry deleted successfully!")
    else:
        messagebox.showerror("Error", "Entry not found.")

#Initialize the database
init_db()

#Create main window
root = tk.Tk()
root.title("Phonebook")
root.geometry("300x250")

#Create UI elements
name_label = tk.Label(root, text="Name:")
name_label.pack()
name_entry = tk.Entry(root)
name_entry.pack()

phone_label = tk.Label(root, text="Phone:")
phone_label.pack()
phone_entry = tk.Entry(root)
phone_entry.pack()

add_button = tk.Button(root, text="Add Entry", command=add_entry)
add_button.pack()

lookup_button = tk.Button(root, text="Lookup Entry", command=lookup_entry)
lookup_button.pack()

update_button = tk.Button(root, text="Update Entry", command=update_entry)
update_button.pack()

delete_button = tk.Button(root, text="Delete Entry", command=delete_entry)
delete_button.pack()

#Run the main loop
root.mainloop()