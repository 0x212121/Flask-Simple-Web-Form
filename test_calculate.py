import unittest
from unittest.main import main
from calculate import calc

class TestCalculate(unittest.TestCase):
    
    def test_calculate(self):
        case1 = ["Ya", "Ya", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak"]
        case2 = ["Tidak", "Tidak", "Tidak", "Ya", "Tidak", "Tidak", "Tidak", "Tidak"]
        case3 = ["Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak", "Tidak"]
        case4 = [True, True, True, True, True, True, True, False]
        
        self.assertEqual(calc(case1), "Direkomendasikan")
        self.assertEqual(calc(case2), "Direkomendasikan")
        self.assertEqual(calc(case3), "Tidak direkomendasikan")
        self.assertEqual(calc(case4), "Tidak direkomendasikan")

if __name__ == '__main__':
    unittest.main()