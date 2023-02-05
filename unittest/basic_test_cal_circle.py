import unittest
import math

def area_of_circle(radius):
    if type(radius) not in [int, float]:
        raise TypeError("Radius must be a number")
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return math.pi * radius**2

class TestAreaOfCircle(unittest.TestCase):
    def test_areas_when_radius_gte_0(self):
        self.assertAlmostEqual(area_of_circle(0), 0)
        self.assertAlmostEqual(area_of_circle(1), math.pi)
        self.assertAlmostEqual(area_of_circle(2), 4 * math.pi)
    
    def test_value_errors_raised(self):
        with self.assertRaises(ValueError):
            area_of_circle(-1)
    
    def test_type_errors_raised(self):
        with self.assertRaises(TypeError):
            area_of_circle("abc")

if __name__ == '__main__':
    unittest.main()
