import random

def generate_secret_number(length):
    """Function to generate a dynamic secret number."""
    secret_number = []
    for _ in range(length):
        secret_number.append(random.randint(0, 3))  # Generate a random digit between 0 and 3
    print(secret_number)
    return secret_number

def secret_number_game(secret_number):
    while True:
        try:
            guess = input("Guess the secret number: ")

            # Convert the guess and secret number to integers
            guess = int(guess)
            secret_number_int = int(''.join(str(digit) for digit in secret_number))

            # Compare the guess with the secret number
            if guess == secret_number_int:
                print("Congratulations! You guessed the secret number correctly!")
            elif guess < secret_number_int:
                print("Your guess is too low.")
            else:
                print("Your guess is too high.")

        except ValueError:
            print("Invalid input! Please enter a sequence of digits only.")

        while True:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == 'yes' or play_again.lower() == 'no':
                break
            else:
                print("Invalid input! Please enter 'yes' or 'no' only.")

        if play_again.lower() != 'yes':
            print("Thank you for playing the Secret Number Game. Goodbye!")
            break

# Generate a secret number with 2 digits
secret_number_length = 2
secret_number = generate_secret_number(secret_number_length)
secret_number_game(secret_number)
