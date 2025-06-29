from datetime import datetime
from app.translations import TRANSLATIONS

def salutation_selon_heure(translations, heure=None):
    if heure is None:
        heure = datetime.now().hour
    return translations["greeting_evening"] if heure > 16 else translations["greeting_day"]

def analyser_texte(string):
    mot_inverse = string[::-1]
    est_palindrome = string == mot_inverse
    return mot_inverse, est_palindrome

def run(string=None, langue="fr", mode_test=False):
    translations = TRANSLATIONS.get(langue, TRANSLATIONS["fr"])
    print(salutation_selon_heure(translations))

    while string != "exit":
        if string is None:
            if mode_test:
                break
            string = input(translations["prompt"])

        if string == "exit":
            print(translations["bye"])
            break

        mot_inverse, est_palindrome = analyser_texte(string)
        print(translations["reversed"], mot_inverse)
        print(translations["good_job"] if est_palindrome else translations["try_again"])

        if mode_test:
            print(translations["bye"])
            break

        string = None



if __name__ == "__main__":
    run()