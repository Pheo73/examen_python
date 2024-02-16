import unittest

def est_palindrome(chaine):
    chaine_inverse = chaine[::-1]
    return chaine == chaine_inverse

class TestEstPalindrome(unittest.TestCase):

    def test_palindrome_normal(self):
        self.assertTrue(est_palindrome("radar"))

    def test_palindrome_avec_espaces(self):
        self.assertFalse(est_palindrome("un été"))

    def test_non_palindrome(self):
        self.assertFalse(est_palindrome("python"))

    def test_palindrome_majuscules_minuscules(self):
        self.assertFalse(est_palindrome("Madam"))

    def test_palindrome_majuscules_minuscules_avec_espaces(self):
        self.assertFalse(est_palindrome("Ésope reste ici et se repose"))

    def test_chaine_vide(self):
        self.assertTrue(est_palindrome(""))

    def test_espaces_seuls(self):
        self.assertTrue(est_palindrome("   "))

if __name__ == '__main__':
    unittest.main()
