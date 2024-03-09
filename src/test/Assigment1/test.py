import unittest
from python_assignment.src.assignment1.util import cal_avg


class MyTestCase(unittest.TestCase):
    def cal_avg(self):
        scores = {'Krishna': [67, 68, 69],
                  'Arjun': [70, 98, 63],
                  'Malika': [52, 56, 60]}
        s = input()
        op = cal_avg(scores, s)
        expected = 56.0
        self.assertEqual(op, expected)  # add assertion here


if __name__ == '__main__':
    unittest.main()
