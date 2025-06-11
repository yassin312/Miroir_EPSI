# tests/test_main.py
import unittest
from app import main

class TestMain(unittest.TestCase):

    def test_salutation_matin(self):
        # ETANT DONNE 
        # QUAND il est 8h
        # ALORS on obtient "Bonjour"
        self.assertEqual(main.salutation_selon_heure(8), "Bonjour")

    def test_salutation_soir(self):
        # ETANT DONNE 
        # QUAND il est 23h
        # ALORS on obtient "Bonsoir"
        self.assertEqual(main.salutation_selon_heure(23), "Bonsoir")

    def test_analyse_palindrome(self):
        # ETANT DONNE 
        # QUAND le mot est kayak
        # ALORS on obtient le même mot good job
        mot_inverse, est_palindrome = main.analyser_texte("kayak")
        self.assertEqual(mot_inverse, "kayak")
        self.assertTrue(est_palindrome)

    def test_analyse_non_palindrome(self):
        # ETANT DONNE 
        # QUAND le mot est mathieu
        # ALORS on obtient le mot à l'envers et Essaye encore
        mot_inverse, est_palindrome = main.analyser_texte("mathieu")
        self.assertEqual(mot_inverse, "ueihtam")
        self.assertFalse(est_palindrome)

if __name__ == '__main__':
    unittest.main()