import tkinter as tk
from tkinter import ttk

class App:
    def __init__(self, root):
        self.root = root
        self.root.title("Progress Bar App")
        
        self.num = 0
        self.history = []

        # Label to display the current number
        self.label = tk.Label(root, text="Number: 0", font=("Arial", 14))
        self.label.pack(pady=10)

        # Progress bar
        self.progress = ttk.Progressbar(root, orient="horizontal", length=300, mode="determinate")
        self.progress.pack(pady=10)
        self.update_progress()

        # Buttons to add and subtract
        self.add_button = tk.Button(root, text="Add", command=self.add_one)
        self.add_button.pack(side="left", padx=10)
        
        self.sub_button = tk.Button(root, text="Subtract", command=self.subtract_one)
        self.sub_button.pack(side="right", padx=10)

        # Buttons for undo and redo
        self.undo_button = tk.Button(root, text="Undo", command=self.undo)
        self.undo_button.pack(side="left", padx=10)
        
        self.redo_button = tk.Button(root, text="Redo", command=self.redo)
        self.redo_button.pack(side="right", padx=10)

    def update_progress(self):
        self.progress['value'] = (self.num / 150) * 100
        self.label.config(text=f"Number: {self.num}")

    def add_one(self):
        if self.num < 150:
            self.history.append(self.num)
            self.num += 1
            self.update_progress()

    def subtract_one(self):
        if self.num > 0:
            self.history.append(self.num)
            self.num -= 1
            self.update_progress()

    def undo(self):
        if self.history:
            self.num = self.history.pop()
            self.update_progress()

    def redo(self):
        # For simplicity, let's say redo will just add 1 back if it was undone
        if self.num < 150:
            self.num += 1
            self.update_progress()

if __name__ == "__main__":
    root = tk.Tk()
    app = App(root)
    root.mainloop()
