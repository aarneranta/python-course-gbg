# polyinput.py
# Hjälpfunktion för att ta in polygoner som indata grafiskt
# från användaren (överkurs!)
#  -- Ruben Seyer (grupp 7)

# OBS: Du behöver matplotlib och numpy installerade.
#      Om din miljö är korrekt inställd kan det räcka
#      att köra kommandot `pip install matplotlib numpy`.
#      På Chalmers labbdatorer är dessa bibliotek förinstallerade.
import numpy as np
import matplotlib.pyplot as plt

def polyinput(n=-1):
    # Ställ in och visa plot
    plt.clf()
    plt.setp(plt.gca(), autoscale_on=False)
    lab = str(n) + '-' if n >= 0 else 'poly'
    end = ' - right click to end' if n < 0 else ''
    plt.title(f'Input a {lab}gon with your mouse{end}')
    plt.show(block=False)

    # Hämta punkterna med matplotlib.plot.ginput
    # Om n är -1 hämtar vi godtyckligt många, annars hämtar vi max n
    points = np.asarray(plt.ginput(n, timeout=-1, mouse_stop=3, mouse_pop=2))
    
    # Rita ut polygonen
    plt.fill(points[:,0], points[:,1], 'r', lw=2)
    plt.draw()

    # Pausa så man kan se polygonen
    plt.title("Click to close")
    plt.waitforbuttonpress()
    plt.close()
    return points

# Om vi kör som ett skript visar vi punkterna
if __name__ == '__main__':
    print(polyinput())
