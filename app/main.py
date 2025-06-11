# app/main.py
from datetime import datetime

def salutation_selon_heure( langue="fr", heure=None):
    if heure is None:
        heure = datetime.now().hour
    if langue == "en":
        return "Good Evening" if heure > 16 else "Good Afternoon"
    else:
        return "Bonsoir" if heure > 16 else "Bonjour"

def analyser_texte(string):
    mot_inverse = string[::-1]
    est_palindrome = string == mot_inverse
    return mot_inverse, est_palindrome

def run(string, langue= "fr"):
    print(salutation_selon_heure(langue=langue))
    print(string)
    mot_inverse, est_palindrome = analyser_texte(string)
    if langue == "en":
        print("Reversed word:", mot_inverse)
        if est_palindrome:
            print("Good job")
        else:
            print("Try again")
        print("Goodbye")
    else:
        print("mot inversé :", mot_inverse)
        if est_palindrome:
            print("Good job")
        else:
            print("Essaye encore")
        print("Au revoir")

if __name__ == "__main__":
    run("kayak", "fr")
