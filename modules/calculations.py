"""
Définition des fonctions pour les calculs de la 
calculatrice
"""
a = int(input("Ecrivez le premier nombre: "))
b = int(input("Ecrivez le deuxieme nombre: "))
def addition():
    print(a + b) 

def soustraction():
    print(a - b)

def multiplication():
    print(a * b)

def division():
    if b != 0:
        print(a / b)
    else:
        print("Erreur: Division par zéro")
# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    addition()
    soustraction()
    multiplication()
    division()