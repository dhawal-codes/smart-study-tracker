import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from tracker import add_session, get_sessions, get_total_minutes
from analytics import show_subject_chart


# Button hover effect (change color when mouse enters)
def on_enter(e):
    e.widget["background"] = "#2980b9"


# Restore button color when mouse leaves
def on_leave(e):
    e.widget["background"] = "#3498db"


# GUI window to add a new study session
def add_session_gui():
    win = tk.Toplevel(window)
    win.title("Add Study Session")
    win.geometry("300x200")

    tk.Label(win, text="Subject").pack()
    subject = tk.Entry(win)
    subject.pack()

    tk.Label(win, text="Minutes").pack()
    minutes = tk.Entry(win)
    minutes.pack()

    # Save study session
    def submit():
        if subject.get() == "" or minutes.get() == "":
            messagebox.showerror("Error", "Please fill all fields")
            return

        add_session(subject.get(), minutes.get())
        win.destroy()

    tk.Button(win, text="Submit", command=submit).pack(pady=5)
    tk.Button(win, text="Back", command=win.destroy).pack(pady=5)


# Display all study sessions in table format
def view_sessions():
    win = tk.Toplevel(window)
    win.title("Study Sessions")
    win.geometry("700x400")

    frame = tk.Frame(win)
    frame.pack(fill="both", expand=True)

    tree = ttk.Treeview(frame, columns=("ID", "Subject", "Minutes", "Date"), show="headings")

    tree.heading("ID", text="ID")
    tree.heading("Subject", text="Subject")
    tree.heading("Minutes", text="Minutes")
    tree.heading("Date", text="Date")

    tree.column("ID", width=60, anchor="center")
    tree.column("Subject", width=200)
    tree.column("Minutes", width=80, anchor="center")
    tree.column("Date", width=200)

    # Add vertical scrollbar
    scroll = ttk.Scrollbar(frame, orient="vertical", command=tree.yview)
    tree.configure(yscrollcommand=scroll.set)

    scroll.pack(side="right", fill="y")
    tree.pack(fill="both", expand=True)

    # Load sessions from database
    sessions = get_sessions()

    # Insert data into table
    for s in sessions:
        tree.insert("", tk.END, values=s)

    tk.Button(win, text="Back", command=win.destroy).pack(pady=10)


# Show total study time
def show_total():
    win = tk.Toplevel(window)
    win.title("Total Study Time")
    win.geometry("250x150")

    total = get_total_minutes()

    tk.Label(win, text=f"Total Minutes Studied : {total}", font=("Segoe UI", 12)).pack(pady=30)

    tk.Button(win, text="Back", command=win.destroy).pack()


# Main GUI function
def run_gui():
    global window

    window = tk.Tk()
    window.title("Smart Study Tracker")
    window.configure(bg="#f4f6f7")

    window.geometry("500x450")

    # Center window on screen
    screen_width = window.winfo_screenwidth()
    screen_height = window.winfo_screenheight()
    x = (screen_width / 2) - (500 / 2)
    y = (screen_height / 2) - (450 / 2)

    window.geometry(f"500x450+{int(x)}+{int(y)}")
    window.resizable(False, False)

    # Title label
    title = tk.Label(
        window,
        text="Smart Study Tracker",
        font=("Segoe UI", 20, "bold"),
        bg="#f4f6f7",
        fg="#2c3e50"
    )
    title.pack(pady=30)

    button_frame = tk.Frame(window, bg="#f4f6f7")
    button_frame.pack()

    # Button style dictionary
    btn_style = {
        "width": 25,
        "height": 1,
        "font": ("Segoe UI", 11),
        "bg": "#3498db",
        "fg": "white",
        "bd": 0,
        "cursor": "hand2",
        "pady": 5
    }

    # List of buttons and their functions
    buttons = [
        ("Add Study Session", add_session_gui),
        ("View Sessions", view_sessions),
        ("Show Analytics", show_subject_chart),
        ("Total Study Time", show_total)
    ]

    # Create buttons dynamically
    for text, cmd in buttons:
        b = tk.Button(button_frame, text=text, command=cmd, **btn_style)
        b.pack(pady=6)
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", on_leave)

    # Exit button
    exit_btn = tk.Button(
        window,
        text="Exit",
        width=25,
        font=("Segoe UI", 11),
        bg="#e74c3c",
        fg="white",
        bd=0,
        cursor="hand2",
        command=window.destroy
    )
    exit_btn.pack(pady=20)

    # Run the application
    window.mainloop()
