import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from function import map
from function import vehicle
from function import autonomous_vehicle
import matplotlib.pyplot as plt

obstacles = [
    (0,0), (0,1), (0,2), (0,3), (0,4),
    (1,0), (1,1), (1,2), (1,3), (1,4),
    (2,0), (2,1), (2,2), (2,3), (2,4),
    (3,0), (3,1), (3,2), (3,3), (3,4),
    (4,0), (4,1), (4,2), (4,3), (4,4),

    (2,10), (3,10), (4,10), (5,10), (6,10), (7,10), (8,10),
    (9,10), (10,10), (11,10), (12,10), (13,10), (14,10),
    (15,10), (16,10), (17,10),
 
    (12,5), (12,6), (12,7), (12,8), (12,9), (12,10), (12,11),
    (12,12), (12,13), (12,14), (12,15), (12,16), (12,17),

    (15,15), (15,16), (15,17), (15,18),
    (16,15), (16,16), (16,17), (16,18),
    (17,15), (17,16), (17,17), (17,18),
    (18,15), (18,16), (18,17), (18,18),

    (14,2), (14,3), (14,4), (14,5),
    (15,2), (15,3), (15,4), (15,5),
    (16,2), (16,3), (16,4), (16,5),
    (17,2), (17,3), (17,4), (17,5),

    (6,3), (6,4), (6,5),
    (7,7), (8,7), (9,7),
    (16,12), (17,12), (16,13), (17,13),

    (18,2),(19,2),(13,5)
]

Mapa = map.map(20, 20, obstacles, 5, 0, 19, 14)

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
