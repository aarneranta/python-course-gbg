"""Uppgift 0: importera matplotlib med kommandot nedan!"""

"""{py, python, python3} -m pip install matplotlib"""

"""välj en av {py, python, python3}, kan till exempel se ut som:
    py -m pip install matplotlib
"""

"""Hur man hanterar CSV-filer"""
import numpy as np
import matplotlib.pyplot as plt

## skapa csv-fil
x = np.linspace(0, 2*np.pi)
y = np.cos(x)
np.savetxt("values.csv", np.vstack((x, y)).T, delimiter=",")

#läs data från csv-fil
data = np.genfromtxt("values.csv", delimiter=',')

"""Uppgift 1: Hämta data från values.csv och plotta"""

x, y = data[:,0], data[:,1]

plt.plot(x, y, 'r')
plt.show()

"""Uppgift 2: objektorienterad plottning"""

fig = plt.figure()
ax1 = fig.add_subplot(121)
ax2 = fig.add_subplot(122)

ax1.plot(x,y,'k')
ax2.plot(x,y,'b')
plt.show()

"""Hur man lägger till titlar"""
plt.plot(x, y, "ro", label="Röd linje")
plt.legend()
plt.title("Elias mästerverk")
plt.xlabel("ankor")
plt.ylabel("timmar")
plt.show()

"""Uppgift 3: Återskapa följande:"""
fig = plt.figure()
ax1 = fig.add_subplot(111, polar = True)
ax1.plot(x, y, label = "Rund Data")
ax1.legend()
plt.show()

"""Uppgift 4: Återskapa följande:"""
fig, axs = plt.subplots(2,2)
axs[0,0].plot(x,y,'r')
axs[0,1].plot(x,y,'g.')
axs[1,0].plot(x,y,'b', linewidth=5)
axs[1,1].plot(x,-y,'yx')

axs[0,0].grid()
axs[0,1].set_title("Fyndig titel!")
axs[0,0].set_ylabel("Spännande y-axel!")
axs[1,0].set_xlabel("Spännande x-axel!")
plt.show()

"""Spara figurer i mapp! Notera att det måste finnas en mapp redan!"""
fig.savefig("img/figur.png")
