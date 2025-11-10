import tkinter as tk
from tkinter import messagebox
from datetime import datetime

# Sample movie data
movies = {
    "Inception": {"time": "6:00 PM", "price": 250},
    "Interstellar": {"time": "9:00 PM", "price": 300},
    "Coco": {"time": "4:00 PM", "price": 200},
    "The Dark Knight": {"time": "7:30 PM", "price": 280}
}

# Main application class
class sachinmoqApp:
    def __init__(self, root):
        self.root = root
        self.root.title("🎟️ sachinmoq - Movie Ticket Booking")
        self.root.geometry("400x400")
        self.root.resizable(False, False)

        self.selected_movie = tk.StringVar()
        self.ticket_count = tk.IntVar(value=1)

        self.create_widgets()

    def create_widgets(self):
        tk.Label(self.root, text="Welcome to sacginmoq!", font=("Helvetica", 16, "bold")).pack(pady=10)
        tk.Label(self.root, text="Select a movie:", font=("Helvetica", 12)).pack()

        # Movie dropdown
        movie_menu = tk.OptionMenu(self.root, self.selected_movie, *movies.keys())
        movie_menu.pack(pady=5)

        # Ticket input
        tk.Label(self.root, text="Number of tickets:", font=("Helvetica", 12)).pack()
        tk.Entry(self.root, textvariable=self.ticket_count, width=5).pack(pady=5)

    