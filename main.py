import modules.calculations as calc
import modules.cli as cli
import modules.animations as anim

"""
Point de lancement du programme
"""

options = ["Calculatrice", "Animation", "Quitter"]

def initialise():
    """() -> None"""
    cli.clear()
    cli.greet()

def loop():
    """() -> None"""
    while (True):
        choix = cli.menu(options)
        if choix == "1":
            loopCalc()
        elif choix == "2":
            anim.animate()
        elif choix == "3":
            break
        return 

def loopCalc():
    """() -> None"""
    while (True):
        choix = cli.menuCalc()
        if choix == "1":
            calc.addition()
        elif choix == "2":
            calc.soustraction()
        elif choix == "3":
            calc.multiplication()
        elif choix == "4":
            calc.division()
        elif choix == "5":
            loop()
        return 

def terminate():
    """() -> None"""
    cli.close()


if __name__ == "__main__":
    # Logique globale du programme (menu infini avec option de sortie)
    initialise()
    loop()
    terminate()