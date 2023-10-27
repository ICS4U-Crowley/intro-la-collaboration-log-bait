import os

"""
Définitions des méthodes pour l'interface de ligne de commande,
l'interface utilisateur à la console
"""


def greet():
    """() -> None"""
    # Afficher un message d'acceuil
    print("Bienvenue à notre programme! Nous effectuerons des calculations et le dessin d'un cercle.")


def menu(items):
    """(list of str) -> str"""
    # Afficher le menu
    print("MENU")
    print("----")
    for i in items:
        print(items.index(i)+1, i)

    return input("> ")


def clear():
    """() -> None"""
    os.system('cls' if os.name == 'nt' else 'clear')


def close():
    """() -> None"""
    # Afficher un message de sortie
    print("Merci d'avoir utilisé notre programme. Au revoir!")


# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":
    # Tests unitaires
    clear()
    greet()
    choix = menu(["op1", "op2", "op3"])
