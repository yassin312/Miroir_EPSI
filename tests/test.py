# tests/test_main.py
import unittest
from unittest.mock import patch
from io import StringIO
from app import main

class TestMain(unittest.TestCase):

    # ETANT DONNE
    # QUAND il est 8h
    # ALORS on obtient "Bonjour"
    def test_salutation_matin(self):
        # Arrange
        heure = 8

        # Act
        resultat = main.salutation_selon_heure(heure=heure, langue="fr")

        # Assert
        self.assertEqual(resultat, "Bonjour")

    # ETANT DONNE
    # QUAND il est 23h
    # ALORS on obtient "Bonsoir"
    def test_salutation_soir(self):
        # Arrange
        heure = 23

        # Act
        resultat = main.salutation_selon_heure(heure=heure, langue="fr")

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

    # ETANT DONNE un utilisateur parlant une langue
    # QUAND on entre un palindrome
    # ALORS il est renvoyé ET le <bienDit> de cette langue est envoyé
    @patch("sys.stdout", new_callable=StringIO)
    def test_palindrome_envoie_bienDit_selon_langue(self, mock_stdout):
        # Arrange
        mot = "radar"

        # Act
        main.run(mot, langue="en")

        # Assert
        output = mock_stdout.getvalue()
        self.assertIn("Good job", output)
        self.assertIn("Reversed word: radar", output)

    # ETANT DONNE un utilisateur parlant une langue
    # QUAND on saisit une chaîne
    # ALORS <bonjour> de cette langue est envoyé avant tout
    @patch("sys.stdout", new_callable=StringIO)
    def test_bonjour_en_premier_selon_langue(self, mock_stdout):
        # Arrange
        mot = "hello"

        # Act
        main.run(mot, langue="en")

        # Assert
        output = mock_stdout.getvalue().splitlines()
        self.assertIn(output[0], ["Good Afternoon", "Good Evening"])

    # ETANT DONNE un utilisateur parlant une langue
    # QUAND on saisit une chaîne
    # ALORS <auRevoir> dans cette langue est envoyé en dernier
    @patch("sys.stdout", new_callable=StringIO)
    def test_au_revoir_en_dernier_selon_langue(self, mock_stdout):
        # Arrange
        mot = "world"

        # Act
        main.run(mot, langue="fr")

        # Assert
        output = mock_stdout.getvalue().strip().splitlines()
        self.assertEqual(output[-1], "Au revoir")

        # Pour la version anglaise aussi :
        mock_stdout.truncate(0)
        mock_stdout.seek(0)
        main.run(mot, langue="en")
        output_en = mock_stdout.getvalue().strip().splitlines()
        self.assertEqual(output_en[-1], "Goodbye")

if __name__ == '__main__':
    unittest.main()
