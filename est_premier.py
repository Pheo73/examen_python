import unittest

def est_premier(nombre):
    if nombre < 2:
        return False
    for i in range(2, int(nombre ** 0.5) + 1):
        if nombre % i == 0:
            return False
    return True

class TestEstPremier(unittest.TestCase):

    def test_nombres_negatifs(self):
        self.assertFalse(est_premier(-5))
        self.assertFalse(est_premier(-1))
        self.assertFalse(est_premier(0))

    def test_nombres_non_premiers(self):
        self.assertFalse(est_premier(1))
        self.assertFalse(est_premier(4))
        self.assertFalse(est_premier(10))
        self.assertFalse(est_premier(100))

    def test_nombres_premiers(self):
        self.assertTrue(est_premier(2))
        self.assertTrue(est_premier(3))
        self.assertTrue(est_premier(7))
        self.assertTrue(est_premier(11))
        self.assertTrue(est_premier(13))
        self.assertTrue(est_premier(17))

    def test_grands_nombres_premiers(self):
        self.assertTrue(est_premier(997))
        self.assertTrue(est_premier(104729))

    def test_grands_nombres_non_premiers(self):
        self.assertFalse(est_premier(1000))
        self.assertFalse(est_premier(99999))

if __name__ == '__main__':
    unittest.main()
