import unittest
from main import get_intersection

class TestSetIntersection(unittest.TestCase):
    def test_intersection(self):
        int_set_1 = {23, 45, 12, 7}
        int_set_2 = {70, 60, 12, 6, 9}
        expected_result = {12, 60}
        result = get_intersection(int_set_1, int_set_2)
        self.assertEqual(result, expected_result)

    def test_empty_intersection(self):
        int_set_1 = {1, 2, 3}
        int_set_2 = {4, 5, 6}
        expected_result = set()
        result = get_intersection(int_set_1, int_set_2)
        self.assertEqual(result, expected_result)

    def test_single_element_intersection(self):
        int_set_1 = {1, 2, 3}
        int_set_2 = {3, 4, 5}
        expected_result = {3}
        result = get_intersection(int_set_1, int_set_2)
        self.assertEqual(result, expected_result)

if __name__ == "__main__":
    unittest.main()
