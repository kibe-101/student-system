import mysql.connector
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

def insert_record():
    fullname = entry_fullname.get()
    course = combo_course.get()
    city = entry_city.get()

    # Check if any field is empty
    if not fullname or not course or not city:
        messagebox.showerror("Error", "Please fill in all fields.")
        return

    try:
        # Establishing a connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='Kibet',
            password='Password',
            database='student'
        )
        cursor = connection.cursor()

        # Constructing the SQL INSERT query
        insert_query = """
        INSERT INTO admission (Fullname, Course, City)
        VALUES (%s, %s, %s)
        """
        
        # Values for the new record
        new_record_values = (fullname, course, city)

        # Executing the SQL INSERT query
        cursor.execute(insert_query, new_record_values)

        # Committing the transaction
        connection.commit()
        print("Record inserted successfully!")

        # Clear input fields after insertion
        entry_fullname.delete(0, tk.END)
        combo_course.set('')
        entry_city.delete(0, tk.END)

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)

    finally:
        # Closing the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

def display_records():
    try:
        # Establishing a connection to the database
        connection = mysql.connector.connect(
            host='localhost',
            user='Kibet',
            password='Password',
            database='student'
        )
        cursor = connection.cursor()

        # Query to retrieve all records from the database
        select_query = "SELECT * FROM admission"
        
        # Executing the SQL SELECT query
        cursor.execute(select_query)

        # Fetch all records
        records = cursor.fetchall()

        # Create a new window to display records
        display_window = tk.Toplevel(root)
        display_window.title("Records")
        display_window.geometry("600x400")
        display_window.configure(background="beige")

        # Create a treeview widget to display records
        tree = ttk.Treeview(display_window, columns=("Fullname", "Course", "City"), show="headings")
        tree.heading("Fullname", text="Fullname")
        tree.heading("Course", text="Course")
        tree.heading("City", text="City")

        # Inserting records into the treeview
        for record in records:
            tree.insert("", tk.END, values=record)

        tree.pack(expand=True, fill=tk.BOTH, padx=10, pady=10)

    except mysql.connector.Error as error:
        print("Failed to connect to MySQL database:", error)

    finally:
        # Closing the cursor and connection
        if 'connection' in locals() or 'connection' in globals():
            cursor.close()
            connection.close()
            print("MySQL connection is closed.")

# Create the main GUI window
root = tk.Tk()
root.title("University Admission System")
root.geometry("400x300")
root.configure(background="beige")

# Style for input fields
style = ttk.Style()
style.configure("TEntry", font=("Arial", 10), foreground="black", background="white", padding=5)

# Label and entry for Fullname
label_fullname = ttk.Label(root, text="Fullname:", background="beige")
label_fullname.grid(row=0, column=0, padx=10, pady=10, sticky="w")
entry_fullname = ttk.Entry(root)
entry_fullname.grid(row=0, column=1, padx=10, pady=10)

# Label and dropdown for Course
label_course = ttk.Label(root, text="Course:", background="beige")
label_course.grid(row=1, column=0, padx=10, pady=10, sticky="w")
courses = ["Computer Science", "Electrical Engineering", "Psychology", "Biology", "Business Administration", "English Literature", "Mathematics", "Civil Engineering", "Nursing", "Economics"]
combo_course = ttk.Combobox(root, values=courses)
combo_course.grid(row=1, column=1, padx=10, pady=10)

# Label and entry for City
label_city = ttk.Label(root, text="City:", background="beige")
label_city.grid(row=2, column=0, padx=10, pady=10, sticky="w")
entry_city = ttk.Entry(root)
entry_city.grid(row=2, column=1, padx=10, pady=10)

# Button to insert record
insert_button = ttk.Button(root, text="Insert Record", command=insert_record, style="TButton")
insert_button.grid(row=3, columnspan=2, padx=10, pady=10)

# Button to display records
display_button = ttk.Button(root, text="Display Records", command=display_records, style="TButton")
display_button.grid(row=4, columnspan=2, padx=10, pady=10)

# Styling the buttons
style.configure("TButton", background="beige")

# Start the Tkinter event loop
root.mainloop()
