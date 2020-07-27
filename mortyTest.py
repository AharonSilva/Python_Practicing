import unittest
from morty import Morty

class MortyTests(unittest.TestCase):

    def test_universe(self):
        morty = Morty(111)
        self.assertEqual(morty.universe, 111)

    def test_is_assigned(self):
        morty = Morty(111)
        self.assertFalse(morty.is_assigned)

if __name__ == '__name__':
    unittest.main()