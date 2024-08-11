import unittest

from coder.computer_coder import ComputerCoder
from main import print_hi
from rater.computer_rater import ComputerRater


class MyTestCase(unittest.TestCase):
    def test_something(self):
        ComputerRater()
        ComputerCoder()

        self.assertEqual(print_hi("test"), "test")  # add assertion here
