import matplotlib.pyplot as plt 
import numpy as np

class map:

    def __init__(self,width,height,obstacles,startx,starty,goalx,goaly):
        """
        Trieda reprezentujúca prostredie simulácie.
        width: šírka mapy
        height: výška mapy
        obstacles: zoznam prekážok vo forme [(x1,y1),(x2,y2),...]
        startx, starty: počiatočné súradnice
        goalx, goaly: cieľové súradnice
        """
        self.width = width
        self.height = height
        self.obstacles = obstacles
        self.startx = startx
        self.starty = starty
        self.goalx = goalx
        self.goaly = goaly

        # --- Kontrola štartu ---
        if not (0 <= self.startx < width) or not (0 <= self.starty < height):
            raise ValueError(f"Chyba: Štartová pozícia {(self.startx,self.starty)} je mimo mapy!")

        if (self.startx, self.starty) in obstacles:
            raise ValueError(f"Chyba: Na štartovnej pozícii {(self.startx,self.starty)} je prekážka!")

        # --- Kontrola cieľa ---
        if not (0 <= self.goalx < width) or not (0 <= self.goaly < height):
            raise ValueError(f"Chyba: Cieľová pozícia {(self.goalx,self.goaly)} je mimo mapy!")

        if (self.goalx, self.goaly) in obstacles:
            raise ValueError(f"Chyba: Na cieľovej pozícii {(self.goalx,self.goaly)} je prekážka!")

        # --- Kontrola prekážok ---
        for x, y in obstacles:
            if not (0 <= x < width) or not (0 <= y < height):
                raise ValueError(f"Chyba: Prekážka {(x,y)} je mimo mapy!")

    def draw(self,car):
        # Inicializácia plátna
        #plt.figure(figsize=(self.width, self.height))
        plt.clf()

        # Vykreslenie štartu
        plt.scatter(self.startx,self.starty, c='green', marker='s', s=100, label='Start')

        # Vykreslenie cieľu
        plt.scatter(self.goalx,self.goaly, c='red', marker='s', s=100, label='Goal')

        # Vykreslenie auto a trajektorie pohybu
        plt.scatter(car.x, car.y, c='blue', marker='o', s=100, label='Auto')
        plt.plot(car.path_x, car.path_y, 'b--', label='Trajektória')

        # Vykreslenie prekážok
        if self.obstacles:
            ox, oy = zip(*self.obstacles)
            plt.scatter(ox, oy, c='orange', marker='s', s=200, label='Prekážky')

        # Nastavenie legendy
        plt.legend(loc='upper left')
        # Nastavenie osí 
        plt.xlim(-1, self.width)
        plt.ylim(-1, self.height)
        plt.gca().set_aspect('equal', adjustable='box')
        plt.pause(0.1)
        

    def binarna_mapa(self):
        matica = np.zeros((self.height, self.width))
        #matica[self.goaly][self.goalx] = 2  # Cieľ označený ako 2
        if self.obstacles:
            for (x,y) in self.obstacles:
                matica[y][x] = 1  # Prekážky označené ako 1
        return matica
        