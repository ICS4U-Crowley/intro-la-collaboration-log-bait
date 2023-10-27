"""
Définition des fonctions pour les calculs de la 
calculatrice
"""


def addition():
    a = int(input("Ecrivez le premier nombre: "))
    b = int(input("Ecrivez le deuxieme nombre: "))
    print("\nLa reponse est:", a + b)


def soustraction():
    a = int(input("Ecrivez le premier nombre: "))
    b = int(input("Ecrivez le deuxieme nombre: "))
    print("\nLa reponse est:", a - b)


def multiplication():
    a = int(input("Ecrivez le premier nombre: "))
    b = int(input("Ecrivez le deuxieme nombre: "))
    print("\nLa reponse est:", a * b)


def division():
    a = int(input("Ecrivez le premier nombre: "))
    b = int(input("Ecrivez le deuxieme nombre: "))
    if b != 0:
        print("\nLa reponse est:", a / b)
    else:
        print("Erreur: Division par zéro")


# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":
    addition()
    soustraction()
    multiplication()
    division()
