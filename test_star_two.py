import unittest
from two_star import monkey_eat_peach as mep

class TestStarTwo(unittest.TestCase):
    def test_canEatAllPeaches(self):
        cases = [
            {'peachs': [2, 3, 4, 5],'H': 4, 'expect': 5},
            {'peachs': [2, 3, 4, 5],'H': 3, 'expect': 0},
            {'peachs': [30, 11, 23, 4, 20], 'H':6, 'expect':23}
        ]
        
        for item in cases:
            result = mep.canEatAllPeaches(item['peachs'], item['H'])
            self.assertEqual(result, item['expect'])