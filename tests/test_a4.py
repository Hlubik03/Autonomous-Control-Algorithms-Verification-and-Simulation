import sys
import os


sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import map
from function import vehicle
from function import autonomous_vehicle
import matplotlib.pyplot as plt

Mapa = map.map(20, 20,[(1,1)], 1, 1, 3, 10)
autonome_vehicle = autonomous_vehicle.autonomous_vehicle(Mapa.startx, Mapa.starty, 1, 180, Mapa)

autonome_vehicle.find_path()

for i in range(len(autonome_vehicle.path)):

    nx, ny = autonome_vehicle.path[i]

    autonome_vehicle.x = nx
    autonome_vehicle.y = ny
    autonome_vehicle.path_x.append(nx)
    autonome_vehicle.path_y.append(ny)

    Mapa.draw(autonome_vehicle)
    plt.pause(0.1)   

plt.show()