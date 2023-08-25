import random


class Game:
    def __init__(self):
        self.target_number = random.randint(1000, 9999)
        self.attempts = 0

    def check_guess(self, guess):
        self.attempts += 1
        if guess == self.target_number:
            return f"Correct! You guessed it in {self.attempts} attempt(s)."
        else:
            hint = self.generate_hint(guess)
            return hint

    def generate_hint(self, guess):
        hint = ""
        target_digits = [int(digit) for digit in str(self.target_number)]
        guess_digits = [int(digit) for digit in str(guess)]

        for i in range(4):
            if guess_digits[i] == target_digits[i]:
                hint += "O "
            else:
                hint += "X "

        if guess > self.target_number:
            hint += "Hint: The target number is lower."
        else:
            hint += "Hint: The target number is higher."

        return hint.strip()


if __name__ == "__main__":
    game = Game()
    print("Welcome to Guess the Number!")
    print("Try to guess a four-digit number.")

    while True:
        guess = input("Enter your guess (or 'quit' to exit): ")

        if guess.lower() == 'quit':
            break

        if len(guess) != 4 or not guess.isdigit():
            print("Invalid input. Please enter a four-digit number.")
            continue

        guess = int(guess)
        result = game.check_guess(guess)
        print(result)

        if "Correct" in result:
            play_again = input("Do you want to play again? (yes/no): ")
            if play_again.lower() == 'no':
                break
            else:
                game = Game()
