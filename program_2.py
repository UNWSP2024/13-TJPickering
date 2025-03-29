#Programmer: Timothy Pickering
#Date: 3/28/2025
#Title: Cities.db display

#Required modules
import tkinter as tk
from tkinter import messagebox
import sqlite3

#Function to load and display data from the cities database
def load_data():
    try:
        #Connect to the database
        conn = sqlite3.connect('cities.db')
        cur = conn.cursor()

        #Fetch all cities data
        cur.execute('SELECT * FROM Cities')
        results = cur.fetchall()
        conn.close()

        #Display data in the text widget
        text_display.delete(1.0, tk.END)
        for row in results:
            text_display.insert(tk.END, f'{row[0]:<3}{row[1]:20}{row[2]:,.0f}\n')
    except sqlite3.Error as e:
        messagebox.showerror("Database Error", "Could not load cities.db. Make sure the file exists.")

#Create main application window
root = tk.Tk()
root.title("Cities Database Viewer")
root.geometry("400x300")

#Text widget to display data
text_display = tk.Text(root, width=50, height=15, borderwidth=2, relief="solid")
text_display.pack(padx=10, pady=10)

#Load data automatically on startup
load_data()

#Start the tkinter event loop
root.mainloop()