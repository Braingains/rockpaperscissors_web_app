import unittest

from models.game import Game, play_game
from models.player import *

class TestGame(unittest.TestCase):

    def setUp(self):
        self.Rocky = Player('Rocky', 'Rock')
        self.Sissy = Player('Sissy', "Scissors")
        self.Pepe = Player('Pepe', 'Paper')

    def test_player_has_name(self):
        self.assertEqual('Rocky', self.Rocky.name)

    def test_player_has_choice(self):
        self.assertEqual('Rock', self.Rocky.choice)

    def test_rock_beats_scissors(self):
        self.assertEqual(play_game(self.Rocky.choice, self.Sissy.choice), 'Rock')

    def test_scissors_beats_paper(self):
        self.assertEqual(play_game(self.Sissy.choice, self.Pepe.choice), 'Scissors')

    def test_paper_beats_rock(self):
        self.assertEqual(play_game(self.Pepe.choice, self.Rocky.choice), 'Paper')

    def test_draw(self):
        self.assertEqual(play_game(self.Rocky.choice, self.Rocky.choice), 'Draw')

        