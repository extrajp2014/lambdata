import unittest
from statistic import Statistic


class StatisticTests(unittest.TestCase):
    """Making sure Statistic methods are corrected!"""
    def test_statistic_methods(self):
        """Test mean and variance methods """
        object1 = Statistic(numbers = [1,2], confidence=0.95)
        self.assertEqual(object1.mean(), 1.5)
        self.assertEqual(object1.variance(), 0.5)

if __name__ == '__main__':
    unittest.main()