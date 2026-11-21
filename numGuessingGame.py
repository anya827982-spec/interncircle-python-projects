import random
import string
from collections import Counter


# ---------------- NUMBER GUESSING GAME ----------------

def number_guessing_game():
    secret_number = random.randint(1, 100)

    max_attempts = 10
    attempts = 0
    score = 100

    print("\n===== NUMBER GUESSING GAME =====")
    print("Guess a number between 1 and 100")
    print("You have 10 attempts.")

    while attempts < max_attempts:
        try:
            guess = int(input("Enter your guess: "))

            if guess < 1 or guess > 100:
                print("Please enter a number between 1 and 100.")
                continue

            attempts += 1

            if guess == secret_number:
                print("\n🎉 Correct! You guessed the number.")
                print("Attempts:", attempts)
                print("Score:", score)
                return score

            elif guess < secret_number:
                print("Too low!")

            else:
                print("Too high!")

            score -= 10

        except ValueError:
            print("Invalid input! Please enter a whole number.")

    print("\n❌ You ran out of attempts.")
    print("The secret number was:", secret_number)
    print("Score:", score)

    return score


# ---------------- WORD COUNTER ----------------

def count_words(path):
    try:
        with open(path, encoding="utf-8") as file:
            text = file.read().lower()

    except FileNotFoundError:
        print("File not found:", path)
        return None

    # Remove punctuation
    text = text.translate(
        str.maketrans("", "", string.punctuation)
    )

    # Split text into words
    words = text.split()

    # Count words
    return Counter(words)


def word_counter():
    print("\n===== WORD COUNTER =====")

    path = input("Enter file name (example: sample.txt): ")

    counts = count_words(path)

    if counts:
        print("\nTotal words:", sum(counts.values()))
        print("Unique words:", len(counts))

        print("\nTop 10 most common words:")
        print("--------------------------")

        for word, count in counts.most_common(10):
            print(f"{word:<15}{count:>5}")


# ---------------- MAIN MENU ----------------

def main():
    best_score = 0

    while True:
        print("1. Play Number Guessing Game")
        print("2. Count Words in a File")
        print("3. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":

            score = number_guessing_game()

            if score > best_score:
                best_score = score
                print("🏆 New Best Score!")

            print("Best Score:", best_score)

            play_again = input("\nPlay again? (y/n): ").lower()

            if play_again != "y":
                print("Returning to main menu...")

        elif choice == "2":
            word_counter()

        elif choice == "3":
            print("\nThank you for using Project 02!")
            break

        else:
            print("Invalid choice! Please select 1, 2 or 3.")


# Start the program
main()