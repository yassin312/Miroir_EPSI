# app/main.py
from datetime import datetime

def salutation_selon_heure(heure=None):
    if heure==None:
        heure = datetime.now().hour
    return "Bonsoir" if heure > 16 else "Bonjour"

def analyser_texte(string):
    mot_inverse = string[::-1]
    est_palindrome = string == mot_inverse
    return mot_inverse, est_palindrome

def run():
    print(salutation_selon_heure())
    string = ""
    while string != "exit":
        string = input("Entrez votre phrase : ")
        print(string)
        mot_inverse, est_palindrome = analyser_texte(string)
        print("mot inversé :", mot_inverse)
        if est_palindrome:
            print("Good job")
        else:
            print("Essaye encore")
    print("AU revoir")

if __name__ == "__main__":
    run()
