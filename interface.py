import tkinter as tk
import quiz

# Create the main window
root = tk.Tk()
root.title("Quiz App")
root.geometry("400x400")

# Create a label to display the question
question_label = tk.Label(root, text="", font=("Arial", 16))
question_label.pack()

# Create a label to display the options
options_label = tk.Label(root, text="", font=("Arial", 12))
options_label.pack()

# Create a label to display the score
score_label = tk.Label(root, text="", font=("Arial", 12))
score_label.pack()


root.mainloop()