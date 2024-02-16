import unittest

def compter_mots(phrase):
    if not phrase:
        return 0
    else:
        mots = phrase.split()
        return len(mots)

class TestCompterMots(unittest.TestCase):

    def test_phrase_non_vide(self):
        self.assertEqual(compter_mots("Ceci est un exemple"), 4)

    def test_phrase_vide(self):
        self.assertEqual(compter_mots(""), 0)

    def test_phrase_avec_espaces_supplementaires(self):
        self.assertEqual(compter_mots("   Espaces    supplémentaires   "), 2)

    def test_phrase_avec_seulement_espaces(self):
        self.assertEqual(compter_mots("       "), 0)

    def test_phrase_avec_seulement_nouveaux_caracteres(self):
        self.assertEqual(compter_mots("\n\n\n"), 0)

    def test_phrase_avec_seulement_tabulations(self):
        self.assertEqual(compter_mots("\t\t\t"), 0)

    def test_phrase_avec_seulement_espaces_et_nouveaux_caracteres(self):
        self.assertEqual(compter_mots("  \n  \t  "), 0)

if __name__ == '__main__':
    unittest.main()
