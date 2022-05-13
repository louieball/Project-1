import unittest
from main import *


class MyTestCase(unittest.TestCase):
    def test_square_area(self):
        self.assertEqual(square_area(10), 100)  # SQUARES
        self.assertAlmostEqual(square_area(0.1), 0.01, delta=0.001)

        with self.assertRaises(TypeError):
            square_area('0.1')

        with self.assertRaises(ValueError):
            square_area(0)
            square_area(-1)

    def test_circle_area(self):
        self.assertAlmostEqual(circle_area(3.2), 32.17, delta=0.001)  # CIRCLES
        self.assertAlmostEqual(circle_area(2), 12.566, delta=0.001)

        with self.assertRaises(TypeError):
            circle_area('0.1')

        with self.assertRaises(ValueError):
            circle_area(0)
            circle_area(-1)

    def test_rectangle_area(self):
        self.assertEqual(rectangle_area(10, 2), 20)
        self.assertAlmostEqual(rectangle_area(3.2, 3), 9.60, delta=0.001)  # RECTANGLES
        self.assertAlmostEqual(rectangle_area(2.5, 2.5), 6.25, delta=6.250)
        self.assertAlmostEqual(rectangle_area(3, 3.2), 9.60, delta=0.001)

        with self.assertRaises(TypeError):
            rectangle_area('1', 2)
            rectangle_area('0.1', '0.1')
            rectangle_area(2, '0.1')
            rectangle_area(1, '2')
        with self.assertRaises(ValueError):
            rectangle_area(0, 0)
            rectangle_area(-1, 3)
            rectangle_area(3, -1)
            rectangle_area(-2, -2)
            rectangle_area(0, 1)
            rectangle_area(1, 0)

    def test_triangle_area(self):
        self.assertEqual(triangle_area(10, 2), 10)
        self.assertAlmostEqual(triangle_area(1.5, 1), 0.750, delta=0.001)  # TRIANGLES
        self.assertAlmostEqual(triangle_area(1, 1.5), 0.750, delta=0.001)
        self.assertAlmostEqual(triangle_area(1.5, 1.5), 1.125, delta=0.001)

        with self.assertRaises(TypeError):
            triangle_area('0.1', 5)
            triangle_area('0.1', '0.1')
            triangle_area(2, '0.1')
        with self.assertRaises(ValueError):
            triangle_area(0, 0)
            triangle_area(-1, 3)
            triangle_area(3, -1)
            triangle_area(-2, -2)
            triangle_area(0, 1)
            triangle_area(1, 0)


if __name__ == '__main__':
    unittest.main()