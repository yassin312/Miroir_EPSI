from datetime import datetime

temps = datetime.now()

if ( temps.hour > 16) :
    print("Bonsoir")
else:
    print("Bonjour")

string = ""
mot_inverse = ""
while (string !="exit"):

    string = input("Entrez votre phrase : ")
    print(string)

    mot_inverse = string[::-1]
    print("mot inversé : ",mot_inverse )

    if (string == mot_inverse) :
        print("Good job")
    else:
        print("Essaye encore")

print("AU revoir")
