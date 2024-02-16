import unittest

def calculer_moyenne(liste):
    if not liste:
        return None 
    else:
        return sum(liste) / len(liste)

class TestCalculMoyenne(unittest.TestCase):

    def test_moyenne_liste_non_vide(self):
        resultat = calculer_moyenne([1, 2, 3, 4, 5])
        self.assertEqual(resultat, 3.0)

    def test_moyenne_liste_decimale(self):
        resultat = calculer_moyenne([1.5, 2.5, 3.5])
        self.assertEqual(resultat, 2.5)

    def test_moyenne_liste_vide(self):
        resultat = calculer_moyenne([])
        self.assertIsNone(resultat)

    def test_moyenne_liste_negatif(self):
        resultat = calculer_moyenne([-1, -2, -3, -4, -5])
        self.assertEqual(resultat, -3.0)

    def test_moyenne_liste_melangee(self):
        resultat = calculer_moyenne([2, -1, 5, 0, -3])
        self.assertEqual(resultat, 0.6)

if __name__ == '__main__':
    unittest.main()
