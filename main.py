# Import database connection function
from database import connect_db

# Import GUI runner function
from gui import run_gui

# Initialize the database connection
connect_db()

# Start the graphical user interface
run_gui()
