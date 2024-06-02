import random

def number_guessing_game():
    # Display game introduction and level selection
    print("Welcome to the Number Guessing Game!")
    print("Choose a difficulty level:")
    print("1. Easy (1-10, unlimited attempts)")
    print("2. Medium (1-50, 10 attempts)")
    print("3. Hard (1-100, 5 attempts)")

    level = input("Enter the level number (1, 2, or 3): ")

    # Set range and maximum attempts based on chosen level
    if level == '1':
        max_number = 10
        max_attempts = float('inf')  # Unlimited attempts
    elif level == '2':
        max_number = 50
        max_attempts = 10
    elif level == '3':
        max_number = 100
        max_attempts = 5
    else:
        print("Invalid level choice. Exiting the game.")
        return

    # Generate a random number within the specified range
    secret_number = random.randint(1, max_number)
    attempts = 0
    guess = None

    print(f"I have selected a number between 1 and {max_number}.")
    if max_attempts != float('inf'):
        print(f"You have {max_attempts} attempts to guess it.")

    # Loop until the user guesses the correct number or runs out of attempts
    while guess != secret_number and attempts < max_attempts:
        # Get the user's guess
        try:
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Provide feedback on the guess
            if guess < secret_number:
                print("Too low! Try again.")
            elif guess > secret_number:
                print("Too high! Try again.")
            else:
                print(f"Congratulations! You guessed the number in {attempts} attempts.")
        except ValueError:
            print("Invalid input! Please enter an integer.")

    # If the user runs out of attempts
    if attempts == max_attempts and guess != secret_number:
        print(f"Sorry, you've used all your attempts. The number was {secret_number}.")

# Run the game
if __name__ == "__main__":
    number_guessing_game()
