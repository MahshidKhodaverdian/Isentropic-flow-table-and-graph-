
#Mahshid khodaverdian
#Isentropic Flow
from IPython.display import display
import numpy as np
import pandas as pd
import matplotlib.pylab as plt
mach = np.linspace(0.01, 5, 1001)
def isentropic_flow(gama, mach):
    g = gama - 1
    P = np.power((1 + ((g / 2) * mach**2)), gama / g)
    T = 1 + (((gama - 1) / 2) * mach**2)
    A = (1/mach) * np.power(((1 + ((g / 2) * mach**2)) / ((gama + 1) / 2)), ((gama + 1) / (2 * g)))
    RHO = np.power((1 + (((gama - 1) / 2) * mach**2)), (1 / g))
    return P, T, A, RHO 
gama = 1.4
P, T, A, RHO = isentropic_flow(gama, mach)
Isentropic={'Mach': mach, 'P0/P': P, 'T0/T': T, 'A/Astar': A, 'RHO0/RHO': RHO}
TableOfIsentropic = pd.DataFrame(Isentropic)
TableOfIsentropicPlot = pd.DataFrame(Isentropic, index=mach)
TableOfIsentropicPlot[['P0/P', 'T0/T', 'A/Astar', 'RHO0/RHO']].plot()
display(TableOfIsentropic)
plt.xlim(0, 6)
plt.ylim(0, 7)
plt.title('Isentropic')
plt.xlabel('M')
plt.grid()

plt.show()
