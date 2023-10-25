from turtle import *

def animate():
    print("Action d'animation")
    try:
        t = Turtle()
        for i in range(700):
            t.forward(1)
            t.left(1) # Draw a circle
        mainloop()
    except turtle.Terminator as e:
        print('...la fenêtre a été fermée')

if __name__ == "__main__":  
    animate()