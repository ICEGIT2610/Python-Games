import random

def play_game():
    print("Welcome to the game!")
    name = input("What's your name? ")
    print(f"Hello {name}! Let's get started.")

    num = random.randint(1, 100)
    guesses = 0

    while True:
        guess = input("Guess a number between 1 and 100: ")
        try:
            guess = int(guess)
        except ValueError:
            print("Invalid input. Try again.")
            continue

        guesses += 1
        if guess == num:
            print(f"Congratulations! You guessed the number in {guesses} guesses.")
            break
        elif guess < num:
            print("Too low. Try again.")
        else:
            print("Too high. Try again.")

    play_again = input("Do you want to play again? (Y/N) ")
    if play_again.upper() == "Y":
        play_game()
    else:
        print("Thanks for playing!")
