# tests/test_main.py
import unittest
from app import main

class TestMain(unittest.TestCase):

    # ETANT DONNE
    # QUAND il est 8h
    # ALORS on obtient "Bonjour"
    def test_salutation_matin(self):
        # Arrange
        heure = 8

        # Act
        resultat = main.salutation_selon_heure(heure)

        # Assert
        self.assertEqual(resultat, "Bonjour")

    # ETANT DONNE
    # QUAND il est 23h
    # ALORS on obtient "Bonsoir"
    def test_salutation_soir(self):
        # Arrange
        heure = 23

        # Act
        resultat = main.salutation_selon_heure(heure)

        # Assert
        self.assertEqual(resultat, "Bonsoir")

    # ETANT DONNE
    # QUAND le mot est kayak
    # ALORS on obtient le même mot good job
    def test_analyse_palindrome(self):
        # Arrange
        mot = "kayak"

        # Act
        mot_inverse, est_palindrome = main.analyser_texte(mot)

        # Assert
        self.assertEqual(mot_inverse, "kayak")
        self.assertTrue(est_palindrome)

    # ETANT DONNE
    # QUAND le mot est mathieu
    # ALORS on obtient le mot à l'envers et Essaye encore
    def test_analyse_non_palindrome(self):
        # Arrange
        mot = "mathieu"

        # Act
        mot_inverse, est_palindrome = main.analyser_texte(mot)

        # Assert
        self.assertEqual(mot_inverse, "ueihtam")
        self.assertFalse(est_palindrome)


if __name__ == '__main__':
    unittest.main()