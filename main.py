import modules.calculations as calc
import modules.cli as cli
import modules.animations as anim

"""
Point de lancement du programme
"""

options = ["Calculatrice", "Animation", "Quitter"]
optionsCalc = ["Addition", "Soustraction",
               "Multiplication", "Division", "Quitter"]


def initialise():
    """() -> None"""
    cli.clear()
    cli.greet()


def loop():
    """() -> None"""
    while (True):
        choix = cli.menu(options)
        if choix == "1":
            cli.clear()
            while (True):
                choix = cli.menu(optionsCalc)
                if choix == "1":
                    calc.addition()
                elif choix == "2":
                    calc.soustraction()
                elif choix == "3":
                    calc.multiplication()
                elif choix == "4":
                    calc.division()
                elif choix == "5":
                    break
        elif choix == "2":
            anim.animate()
        elif choix == "3":
            return
        cli.clear()


def terminate():
    """() -> None"""
    cli.close()


if __name__ == "__main__":
    # Logique globale du programme (menu infini avec option de sortie)
    initialise()
    loop()
    terminate()
