import unittest
from cosmicpathoptimization import answer


class TestCosmic(unittest.TestCase):
    def test_answer1(self) -> None:
        self.assertEqual(answer(), 1)
