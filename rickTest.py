import unittest
from rick import Rick
from morty import Morty


class RickTest(unittest.TestCase):

    def test_universe(self):
        rick = Rick(111)
        self.assertEqual(rick.universe, 111)

    def test_has_morty(self):
        rick = Rick(111)
        self.assertEqual(rick.morty, None)

    def test_assign_morty(self):
        rick = Rick(111)
        morty = Morty(111)

        rick.assign(morty)

        self.assertEqual(rick.morty, morty)
        self.assertTrue(morty.is_assigned)

    def test_has_is_pickle(self):
        rick = Rick(111)
        self.assertFalse(rick.is_pickle)


if __name__ == '__name__':
    unittest.main()
