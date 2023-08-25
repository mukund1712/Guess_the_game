import unittest
from main import Game

class TestGuessTheNumberGame(unittest.TestCase):

    def test_generate_random_number(self):
        game = Game()
        self.assertTrue(1000 <= game.target_number <= 9999)

    def generate_hint(self, guess):
        hint = ""
        target_digits = [int(digit) for digit in str(self.target_number)]
        guess_digits = [int(digit) for digit in str(guess)]

        for i in range(4):
            if guess_digits[i] == target_digits[i]:
                hint += "O "
            else:
                hint += "X "

        if guess < self.target_number:
            hint += "(Hint: The target number is higher)"
        else:
            hint += "(Hint: The target number is lower)"

        return hint.strip()

    def test_check_correct_guess(self):
        game = Game()
        game.target_number = 1234
        result = game.check_guess(1234)
        self.assertEqual(result, "Correct! You guessed it in 1 attempt(s).")

    def test_generate_hint(self):
        game = Game()
        game.target_number = 4321
        hint = game.generate_hint(1234)
        self.assertEqual(hint, "X X X X Hint: The target number is higher.")


if __name__ == '__main__':
    unittest.main();