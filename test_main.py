import unittest
from main import get_intersection

class TestSetIntersection(unittest.TestCase):
    def test_intersection(self):
        int_set_1 = {23, 45, 12, 7}
        int_set_2 = {70, 60, 12, 6, 9}
        expected_result = {12, 60}  # Ожидаемый результат
        result = get_intersection(int_set_1, int_set_2)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
