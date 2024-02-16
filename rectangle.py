import unittest

class Rectangle:
    def __init__(self, longueur, largeur):
        self.longueur = longueur
        self.largeur = largeur

    def calculer_perimetre(self):
        return 2 * (self.longueur + self.largeur)

    def calculer_surface(self):
        return self.longueur * self.largeur

class TestRectangleMethods(unittest.TestCase):

    def test_calculer_perimetre(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.calculer_perimetre(), 16)

        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.calculer_perimetre(), 0)

        rectangle = Rectangle(-5, 4)
        self.assertEqual(rectangle.calculer_perimetre(), -2)

    def test_calculer_surface(self):
        rectangle = Rectangle(5, 3)
        self.assertEqual(rectangle.calculer_surface(), 15)

        rectangle = Rectangle(0, 0)
        self.assertEqual(rectangle.calculer_surface(), 0)

        rectangle = Rectangle(-5, 4)
        self.assertEqual(rectangle.calculer_surface(), -20)

if __name__ == '__main__':
    unittest.main()