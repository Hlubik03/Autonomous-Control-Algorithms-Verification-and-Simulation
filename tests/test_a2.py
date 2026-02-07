import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import map
from function import vehicle
from function import autonomous_vehicle
import matplotlib.pyplot as plt

obstacles = [
    
    (1, 1), (1, 2), (2, 1), (2, 2),
    (5, 5), (5, 6), (6, 5), (6, 6),
    (10, 10), (10, 11), (11, 10), (11, 11),
    (15, 3), (16, 3), (15, 4), (16, 4),

    *[(i, 12) for i in range(4, 20)],

    *[(12, j) for j in range(4, 15)]
]


Mapa = map.map(20, 20, obstacles, 0, 0, 19, 19)
autonome_vehicle = autonomous_vehicle.autonomous_vehicle(Mapa.startx, Mapa.starty, 1, 0, Mapa)
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
