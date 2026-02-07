import sys
import os

# root priečinok do sys.path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import map
from function import vehicle
from function import autonomous_vehicle

import matplotlib.pyplot as plt

# Vytvorenie mapy s danými parametrami
Mapa = map.map(20, 20,  [*[(i, 2) for i in range(1, 10)],*[(i, 5) for i in range(0, 19)],*[(i, 8) for i in range(1, 20)],(12,7),(14,6)], 3, 1, 3, 10)

# Inicializácia autonómneho vozidla na začiatku mapy
autonome_vehicle = autonomous_vehicle.autonomous_vehicle(Mapa.startx, Mapa.starty, 1, 180, Mapa)

# Nájdenie cesty autonómnym vozidlom
autonome_vehicle.find_path()

# Prechod cez všetky body na ceste
for i in range(len(autonome_vehicle.path)):
    nx, ny = autonome_vehicle.path[i]

    # Aktualizácia pozície autonómneho vozidla
    autonome_vehicle.x = nx
    autonome_vehicle.y = ny
    autonome_vehicle.path_x.append(nx)  
    autonome_vehicle.path_y.append(ny)  

    # Kreslenie mapy s aktuálnou pozíciou autonómneho vozidla
    Mapa.draw(autonome_vehicle)
    plt.pause(0.1)  

# Zobrazenie výsledného grafu
plt.show()