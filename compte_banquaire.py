import unittest

class CompteBancaire:
    def __init__(self, solde_initial):
        self.solde = solde_initial

    def deposer(self, montant):
        self.solde += montant

    def retirer(self, montant):
        if self.solde < montant:
            raise ValueError("Solde insuffisant")
        self.solde -= montant

    def obtenir_solde(self):
        return self.solde

class TestCompteBancaire(unittest.TestCase):
    def test_solde_initial(self):
        compte = CompteBancaire(100)
        self.assertEqual(compte.obtenir_solde(), 100)

    def test_deposer(self):
        compte = CompteBancaire(100)
        compte.deposer(50)
        self.assertEqual(compte.obtenir_solde(), 150)

    def test_retirer_solde_suffisant(self):
        compte = CompteBancaire(100)
        compte.retirer(50)
        self.assertEqual(compte.obtenir_solde(), 50)

    def test_retirer_solde_insuffisant(self):
        compte = CompteBancaire(100)
        with self.assertRaises(ValueError):
            compte.retirer(150)

    def test_retirer_solde_egale(self):
        compte = CompteBancaire(100)
        compte.retirer(100)
        self.assertEqual(compte.obtenir_solde(), 0)

if __name__ == '__main__':
    unittest.main()