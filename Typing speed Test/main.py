import tkinter as tk
from tkinter import messagebox
import random
import time
from faker import Faker

# Sample random texts for the typing test
fake = Faker()
texts = fake.sentence(50)

class TypingSpeedTestApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Typing Speed Test")

        self.random_text = texts
        self.start_time = None
        self.time_limit = 60  # seconds

        self.text_title = tk.Label(root, text="Measure your Typing Speed", wraplength=400, font=("Impact", 50))
        self.text_title.pack(pady=10)

        # Label to display the random text
        self.text_label = tk.Label(root, text=self.random_text, wraplength=400, font=("Arial", 14))
        self.text_label.pack(pady=10)

        self.text_note = tk.Label(root, text="Just start typing the above to start", wraplength=400, font=("Arial", 7))
        self.text_note.pack(pady=10)

        # Entry field for typing
        self.typing_field = tk.Entry(root, width=50, font=("Arial", 14))
        self.typing_field.pack(pady=10)
        self.typing_field.bind("<KeyPress>", self.start_timer)
        self.typing_field.bind("<Return>", self.calculate_speed) 

         # Button to reset the game
        self.reset_button = tk.Button(root, text="Reset", command=self.reset_game)
        self.reset_button.pack(pady=10)

        # Button to submit
        self.submit_button = tk.Button(root, text="Submit", command=self.calculate_speed)
        self.submit_button.pack(pady=10)



        # Label to display results
        self.result_label = tk.Label(root, text="", font=("Arial", 14))
        self.result_label.pack(pady=10)

    def start_timer(self, event):
        if self.start_time is None:  # Start the timer only on the first key press
            self.start_time = time.time()
            self.root.after(self.time_limit * 1000, self.calculate_speed)

    def reset_game(self):
        self.text_label.config(text = fake.sentence(40))
        self.start_time = None
        self.typing_field.delete(0, tk.END)  # Clear the typing field
        self.result_label.config(text="")
        self.typing_field.config(state=tk.NORMAL)  # Enable typing again

    def calculate_accuracy(self, typed_text, target_text):
        typed_words = typed_text.split()  # Split the typed text into words
        target_words = target_text.split()  # Split the target text into words

        correct_words = sum(1 for typed, target in zip(typed_words, target_words) if typed == target)

        accuracy = (correct_words / len(target_words)) * 100 if len(target_words) > 0 else 0
        return accuracy
    

    def calculate_speed(self):
        if self.start_time is None:
            messagebox.showinfo("Info", "Please start typing to begin the test.")
            return

        elapsed_time = time.time() - self.start_time

        if elapsed_time > self.time_limit:
            elapsed_time = self.time_limit  # Ensure the time is capped at 60 seconds

        typed_text = self.typing_field.get()
        total_characters = len(typed_text)
        total_words = total_characters / 5

        wpm = total_words / (elapsed_time / 60)
        cpm = total_characters / (elapsed_time / 60)

        accuracy = self.calculate_accuracy(typed_text, self.random_text)

        self.result_label.config(
            text=f"Time: {int(elapsed_time)}s\nWPM: {wpm:.2f}\nCPM: {cpm:.2f}\nAccuracy: {accuracy:.2f}%"
        
        )

       
        # Disable further input after time is up
        self.typing_field.config(state=tk.DISABLED)

if __name__ == "__main__":
    root = tk.Tk()
    app = TypingSpeedTestApp(root)
    root.mainloop()
