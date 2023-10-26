"""
Définition des fonctions pour les calculs de la 
calculatrice
"""
def addition(a, b):
    return a + b

def soustraction(a, b):
    return a - b

def multiplication(a, b):
    return a * b

def division(a, b):
    if b != 0:
        return a / b
    else:
        return "Erreur: Division par zéro"
# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    print(addition(5, 3))
    print(soustraction(5, 3))
    print(multiplication(5, 3))
    print(division(6, 2))
    print(division(6, 0))