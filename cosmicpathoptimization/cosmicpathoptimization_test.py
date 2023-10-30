import unittest
from cosmicpathoptimization import answer


class TestCosmic(unittest.TestCase):
    def test_answer1(self) -> None:
        self.assertEqual(answer([317, 281, 314]), 304)

    def test_answer2(self) -> None:
        self.assertEqual(answer([3819, 4696, 2733, 5247, 5902,
                                 3753, 3484, 486, 9698, 581]), 4039)

    def test_answer3(self) -> None:
        self.assertEqual(answer([78088, 85395, 46621, 64019, 66747,
                                 40728, 83634, 78859, 52514, 9201,
                                 35537, 57434, 85481, 93428, 95176,
                                 94316, 40918, 29244, 74640, 10401,
                                 31117, 74636, 90075, 8809, 69030]), 59841)
