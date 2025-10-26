"""
Fatima Nadeem 
10/26/2025
Project 2 Part 2
Unittest 
"""

import unittest
from main import Connect4 # import the main Connect4 class

class TestDropChip(unittest.TestCase):
    def setUp(self):
        # make a new Connect4 game before every test
        self.game = Connect4()
    def test_successful_drop(self):
        # test if a chip drops correctly in an empty column
        result = self.game.drop_chip(0)
        self.assertTrue(result) # should return True
    # just checking if drop works normally
    def test_full_column(self):
        # fill one column completely
        for _ in range(6):
            self.game.drop_chip(0)
        # try dropping one more chip in the same column
        result = self.game.drop_chip(0)
        self.assertFalse(result) # should return False since it's full
    # testing that full columns are handled righ
    def test_invalid_column(self):
        # test for wrong column number
        result = self.game.drop_chip(10)
        self.assertFalse(result)# should return False for invalid column
    # checking that game catches out-of-range inputs
    def test_full_board(self):
        # fill up the whole board
        for col in range(7):
            for _ in range(6):
                self.game.drop_chip(col)
        # try dropping another chip when board is full
        result = self.game.drop_chip(3)
        self.assertFalse(result)# no space left, so should return False
        # makes sure game knows when board is full
if __name__ == '__main__':
    # run all the tests
    unittest.main()