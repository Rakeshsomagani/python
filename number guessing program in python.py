import random

def number_guessing_game():
    # Generate a random number between 1 and 100
    secret_number = random.randint(1, 100)
    
    # Initialize variables
    attempts = 0
    guessed_number = None
    
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100. Can you guess it?")
    
    while guessed_number != secret_number:
        try:
            guessed_number = int(input("Enter your guess: "))
            attempts += 1
            
            if guessed_number < secret_number:
                print("Too low! Try again.")
            elif guessed_number > secret_number:
                print("Too high! Try again.")
        except ValueError:
            print("Please enter a valid number.")

    print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts.")

if __name__ == "__main__":
    number_guessing_game()