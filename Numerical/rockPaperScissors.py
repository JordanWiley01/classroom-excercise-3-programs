import random

# Function to get the computer's guess
def get_computer_guess():
    choices = ["Rock", "Paper", "Scissors"]
    return random.choice(choices)

# Function to perform a case-insensitive comparison
def case_insensitive_equals(str1, str2):
    return str1.lower() == str2.lower()

# Display game instructions
print("Let's play Rock, Paper, Scissors!")
print("Enter Rock, Paper, or Scissors")

# Get user's guess (case-insensitive)
user_guess = input("Your guess: ").capitalize()

# Check if the input is valid
if user_guess not in ["Rock", "Paper", "Scissors"]:
    print("Invalid input. Please enter Rock, Paper, or Scissors.")
else:
    # Get computer's guess
    computer_guess = get_computer_guess()

    # Determine the winner (case-insensitive)
    if case_insensitive_equals(user_guess, "Rock") and case_insensitive_equals(computer_guess, "Scissors"):
        result = "You win!"
    elif case_insensitive_equals(user_guess, "Paper") and case_insensitive_equals(computer_guess, "Rock"):
        result = "You win!"
    elif case_insensitive_equals(user_guess, "Scissors") and case_insensitive_equals(computer_guess, "Paper"):
        result = "You win!"
    elif case_insensitive_equals(user_guess, "Rock") and case_insensitive_equals(computer_guess, "Paper"):
        result = "Computer wins!"
    elif case_insensitive_equals(user_guess, "Paper") and case_insensitive_equals(computer_guess, "Scissors"):
        result = "Computer wins!"
    elif case_insensitive_equals(user_guess, "Scissors") and case_insensitive_equals(computer_guess, "Rock"):
        result = "Computer wins!"
    else:
        result = "It's a draw!"

    # Display the result
    print(f"You chose {user_guess}")
    print(f"The computer chose {computer_guess}")
    print(result)
