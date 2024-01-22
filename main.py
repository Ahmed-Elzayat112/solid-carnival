import tkinter as tk
from tkinter import messagebox
import pypyodbc


def update_total_hours_label():
    try:
        cursor.execute("EXEC displayTotalHours")
        rows = cursor.fetchall()

        # Assuming the stored procedure returns a single value
        if rows:
            total_hours = rows[0][0]
            total_hours_label.config(text=f"Total Study Hours: {total_hours}")
        else:
            total_hours_label.config(text="Total Study Hours: 0")

    except pypyodbc.Error as err:
        messagebox.showerror("Error", f"Error retrieving total hours: {err}")


def insert_data():
    subject_name = subject_name_entry.get()
    date = date_entry.get()
    hours_studied = hours_studied_entry.get()

    try:
        cursor.execute(
            "INSERT INTO student (subject_name,date, hours_studied) VALUES (?,?,?)",
            (subject_name, date, hours_studied),
        )
        connection.commit()
        messagebox.showinfo("Success", "Data inserted successfully!")

    except pypyodbc.Error as err:
        messagebox.showerror("Error", f"Error inserting data: {err}")


# Connect to your SQL Server database
connection = pypyodbc.connect(
    "Driver={SQL Server};" "Server=yourServerName;" "Database=studyHours;"
)
cursor = connection.cursor()


# Create the main window
root = tk.Tk()
root.title("Study Hours Tracker")
root.geometry("720x720")

# Subject Name Entry
subject_name_label = tk.Label(root, text="Subject Name:", font=("arial", 15))
subject_name_label.grid(row=0, column=0, padx=20, pady=10)
subject_name_entry = tk.Entry(root, width=30, bd=2, font=("arial", 15))
subject_name_entry.grid(row=0, column=1, padx=20, pady=10)

# Date Entry
date_label = tk.Label(root, text="Date:", font=("arial", 15))
date_label.grid(row=1, column=0, padx=10, pady=10)
date_entry = tk.Entry(root, width=30, bd=2, font=("arial", 15))
date_entry.grid(row=1, column=1, padx=10, pady=10)

# Hours Studied Entry
hours_studied_label = tk.Label(root, text="Hours Studied:", font=("arial", 15))
hours_studied_label.grid(row=2, column=0, padx=10, pady=10)
hours_studied_entry = tk.Entry(root, width=30, bd=2, font=("arial", 15))
hours_studied_entry.grid(row=2, column=1, padx=10, pady=10)

# Insert Data Button
insert_button = tk.Button(
    root,
    text="Insert Data",
    width=10,
    bg="#84f894",
    padx=10,
    pady=10,
    bd=2,
    font=("Arial", 15),
    command=insert_data,
)
insert_button.grid(row=3, column=1, columnspan=2, pady=10)

# Total Study Hours Label
total_hours_label = tk.Label(root, text="Total Study Hours: 0", font=("Arial", 15))
total_hours_label.grid(row=4, column=1, columnspan=2, pady=10)

# Display Total Study Hours Button
display_hours_button = tk.Button(
    root,
    text="Display Total Study Hours",
    width=20,
    bg="#84e8f8",
    padx=10,
    pady=10,
    bd=2,
    font=("Arial", 15),
    command=update_total_hours_label,
)
display_hours_button.grid(row=5, column=1, columnspan=2, pady=10)

# Run the Tkinter event loop
root.mainloop()

# Close the database connection when the application is closed
connection.close()
