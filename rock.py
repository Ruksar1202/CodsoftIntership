import tkinter as tk
import random

# Function to determine the winner
def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        return "It's a tie!"
    if (
        (user_choice == "rock" and computer_choice == "scissors")
        or (user_choice == "paper" and computer_choice == "rock")
        or (user_choice == "scissors" and computer_choice == "paper")
    ):
        return "You win!"
    else:
        return "Computer wins!"

# Function to update the game result
def play():
    user_choice = user_choice_var.get()
    choices = ["rock", "paper", "scissors"]
    computer_choice = random.choice(choices)
    computer_choice_var.set(computer_choice)

    result = determine_winner(user_choice, computer_choice)
    result_var.set(result)

# Create the main window
window = tk.Tk()
window.title("Rock, Paper, Scissors Game")

# Label for user's choice
user_choice_label = tk.Label(window, text="Your choice:")
user_choice_label.pack()

# Radio buttons for user's choice
user_choice_var = tk.StringVar()
user_choice_var.set("rock")  # Default choice
rock_radio = tk.Radiobutton(window, text="Rock", variable=user_choice_var, value="rock")
paper_radio = tk.Radiobutton(window, text="Paper", variable=user_choice_var, value="paper")
scissors_radio = tk.Radiobutton(window, text="Scissors", variable=user_choice_var, value="scissors")
rock_radio.pack()
paper_radio.pack()
scissors_radio.pack()

# Button to play the game
play_button = tk.Button(window, text="Play", command=play)
play_button.pack()

# Label to display computer's choice
computer_choice_var = tk.StringVar()
computer_choice_label = tk.Label(window, text="Computer's choice:")
computer_choice_label.pack()
computer_choice_display = tk.Label(window, textvariable=computer_choice_var)
computer_choice_display.pack()

# Label to display the result
result_var = tk.StringVar()
result_label = tk.Label(window, text="Result:")
result_label.pack()
result_display = tk.Label(window, textvariable=result_var)
result_display.pack()

# Run the GUI application
window.mainloop()
