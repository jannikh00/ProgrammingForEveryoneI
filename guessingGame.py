import random

# This program implements the guessing game. The player is asked to provide a number between 1-20.
# If he didn't guess the right number after 5 times, he lost the game. If he guessed the right number,
# he won the game.

# Generate a random number between 1 and 20
number_to_guess = random.randint(1, 20)

# Initialize guess count
guess_count = 0

print("Welcome to the guessing game! You have 5 attempts to guess a number between 1 and 20.")

# List that later should show the player the guesses he already took
guess_list = []

# This is the while loop where the game happens. In the loop the player gets asked for a number.
# If the number is right, the game is over and the player won the game.
# If the number is wrong, the game continues and the player gets displayed the number of guesses he
# has left as well as the guesses he has already taken. He has 5 guesses.
# If the last guess is taken wrong, the player will receive what would have been the right number.
while guess_count < 5:
    print("Please enter your guess:")
    guess = int(input())
    guess_count += 1    # counts the guesses the player took
    guess_list.append(guess) # extends the list of taken guesses by the most current guess
    if guess == number_to_guess:
        print(f"Congratulations! {guess} is the right number.")
        break
    elif guess != number_to_guess:
        print(f"Sorry! Your guess is wrong.You have {5-guess_count} guesses left.")
        print(f"Your guesses were: {guess_list}")
        if guess_count == 5:
            print(f"The right number would have been {number_to_guess}.")
            print("Please try another time!")
