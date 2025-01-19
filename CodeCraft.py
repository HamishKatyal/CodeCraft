import tkinter as tk
from tkinter import messagebox
import subprocess
import random

# Create the main application window
app = tk.Tk()
app.title("CodeCraft - Coding Game")

# Global variables for scoring, levels, and questions
score = 0
current_level = 1
questions = {
    1: "Write a Python program to print 'Hello, World!'",
    2: "Calculate the sum of two numbers: 5 and 3",
    3: "Write a Python program to find the factorial of 5",
    4: "Calculate the square of a number: 7",
    5: "Write a Python program to check if a number is prime",
    # Add more questions for different levels
}

# Function to run user code
def run_code():
    global score, current_level
    user_code = code_editor.get("1.0", tk.END)
    try:
        # Execute user code and check if it's correct
        exec(user_code)
        if check_answer(user_code, current_level):
            # Correct answer
            score += 10
            score_label.config(text=f"Score: {score}")
            # Move to the next level
            current_level += 1
            if current_level in questions:
                question_label.config(text=questions[current_level])
                level_label.config(text=f"Level: {current_level}")
            else:
                messagebox.showinfo("Game Over", "Congratulations, you've completed all levels!")
        else:
            messagebox.showerror("Incorrect Answer", "Your answer is incorrect. Please try again.")
    except Exception as e:
        messagebox.showerror("Error", str(e))

# Function to check the answer for the current level
def check_answer(user_code, level):
    if level == 1:
        return user_code.strip() == "print('Hello, World!')"
    elif level == 2:
        return user_code.strip() == "print(3 + 5)"
    elif level == 3:
        return user_code.strip() == "120"  # Factorial of 5
    elif level == 4:
        return user_code.strip() == "7 * 7"  # Square of 7
    elif level == 5:
        return user_code.strip() == "True"  # 5 is prime
    # Add more level-specific answer checks here

# Create a code editor (Text widget)
code_editor = tk.Text(app, width=40, height=15)
code_editor.pack()

# Create a "Run Code" button
run_button = tk.Button(app, text="Run Code", command=run_code)
run_button.pack()

# Create a score display
score_label = tk.Label(app, text=f"Score: {score}")
score_label.pack()

# Create a question label
question_label = tk.Label(app, text=questions[current_level])
question_label.pack()

# Create a level label
level_label = tk.Label(app, text=f"Level: {current_level}")
level_label.pack()

# Start the GUI application
app.mainloop()
