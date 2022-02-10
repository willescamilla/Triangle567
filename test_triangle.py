"""Test file for triangle.py"""
import unittest

from triangle import classify_triangle

class test_triangle(unittest.TestCase):
    """Run all tests"""
    def test_invalid_triangles(self):
        """Run test on invalid triangle with give parameters"""
        self.assertEqual(classify_triangle(1, 3, 5), 'Not A Triangle', '1,3,5 is not a Triangle')
    def test_invalid_triangles2(self):
        """Run test on invalid triangle with give parameters"""
        self.assertEqual(classify_triangle(1, 4, 5), 'Not A Triangle', '1,4,5 is not a Triangle')
    def test_invalid_triangles3(self):
        """Run test on invalid triangle with give parameters"""
        self.assertEqual(classify_triangle(1, 0, 1), 'Not A Triangle', '1,0,1 is not a Triangle')

    def test_right_triangles(self):
        """Run test on right triangle with give parameters"""
        self.assertEqual(classify_triangle(3, 4, 5), 'Right', '3,4,5 is a Right triangle')
    def test_right_triangles2(self):
        """Run test on right triangle with give parameters"""
        self.assertEqual(classify_triangle(5, 3, 4), 'Right', '5,3,4 is a Right triangle')
    def test_right_triangles3(self):
        """Run test on right triangle with give parameters"""
        self.assertEqual(classify_triangle(4, 5, 3), 'Right', '4,5,3 is a Right triangle')

    def test_equilateral_triangles(self):
        """Run test on equilateral triangle with give parameters"""
        self.assertEqual(classify_triangle(1, 1, 1), 'Equilateral', '1,1,1 should be equilateral')
    def test_equilateral_triangles2(self):
        """Run test on equilateral triangle with give parameters"""
        self.assertEqual(classify_triangle(3, 3, 3), 'Equilateral', '3,3,3 should be equilateral')
    def test_equilateral_triangles3(self):
        """Run test on equilateral triangle with give parameters"""
        self.assertEqual(classify_triangle(10, 10, 10),
                         'Equilateral', '10,10,10 should be equilateral')

    def test_isosceles_triangles(self):
        """Run test on isosceles triangle with give parameters"""
        self.assertEqual(classify_triangle(5, 5, 1), 'Isosceles', '5,5,1 should be isosceles')
    def test_isosceles_triangles2(self):
        """Run test on isosceles triangle with give parameters"""
        self.assertEqual(classify_triangle(5, 1, 5), 'Isosceles', '5,1,5 should be isosceles')
    def test_isosceles_triangles3(self):
        """Run test on isosceles triangle with give parameters"""
        self.assertEqual(classify_triangle(1, 5, 5), 'Isosceles', '1,5,5 should be isosceles')

    def test_scalene_triangles(self):
        """Run test on scalene triangle with give parameters"""
        self.assertEqual(classify_triangle(5, 7, 3), 'Scalene', '5,7,3 should be scalene')
    def test_scalene_triangles2(self):
        """Run test on scalene triangle with give parameters"""
        self.assertEqual(classify_triangle(10, 8, 5), 'Scalene', '10,8,5 should be scalene')
    def test_scalene_triangles3(self):
        """Run test on scalene triangle with give parameters"""
        self.assertEqual(classify_triangle(11, 7, 6), 'Scalene', '11,7,6 should be scalene')

#NEW TEST CASES
    def test_invalid1(self):
        """Run test on invalid input with give parameters"""
        self.assertEqual(classify_triangle(201, 500, 19),
                         'Invalid Input', '201,500,19 should be invalid')

    def test_invalid2(self):
        """Run test on invalid input with give parameters"""
        self.assertEqual(classify_triangle(-11, -7, -6),
                         'Invalid Input', '-11,-7,-6 Should be invalid')

if __name__ == '__main__':
    print('Running unit tests')
    unittest.main()
