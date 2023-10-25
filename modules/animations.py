from turtle import *

def animate():
    print("Action d'animation")
    try:
        t = Turtle()
        for i in range(350):
            t.forward(1)
            t.left(1)
        mainloop()
    except Terminator as e:
        print('...la fenêtre a été fermée')

# Code pour tester cette module indépendamment du programme principal
if __name__ == "__main__":  
    animate()
