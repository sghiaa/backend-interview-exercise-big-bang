
import unittest
from game import determine_winner, default_score

class TestGameLogic(unittest.TestCase):

    def test_determine_winner_player_wins(self):
        self.assertEqual(determine_winner("rock", "scissors"), "player")
        self.assertEqual(determine_winner("spock", "scissors"), "player")
        self.assertEqual(determine_winner("lizard", "spock"), "player")

    def test_determine_winner_computer_wins(self):
        self.assertEqual(determine_winner("scissors", "rock"), "computer")
        self.assertEqual(determine_winner("paper", "scissors"), "computer")
        self.assertEqual(determine_winner("spock", "lizard"), "computer")

    def test_determine_winner_tie(self):
        self.assertEqual(determine_winner("rock", "rock"), "tie")
        self.assertEqual(determine_winner("spock", "spock"), "tie")

    def test_default_score(self):
        expected = {
            "You": {"wins": 0, "losses": 0, "ties": 0},
            "Computer": {"wins": 0, "losses": 0, "ties": 0},
        }
        self.assertEqual(default_score(), expected)

if __name__ == "__main__":
    unittest.main()
