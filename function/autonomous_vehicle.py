import function.vehicle as vehicle
import function.map as map
from collections import deque

class autonomous_vehicle(vehicle.vehicle):
    def __init__(self,x,y,speed,direction,mapa):

        """
        Podtrieda reprezentujúca autómne vozidlo.
        x,y,speed,direction: parametre zdedené z triedy vehicle
        mapa: inštancia triedy map obsahujúca informácie o mape
        """

        super().__init__(x,y,speed,direction)

        self.mapa = mapa
        self.goal = (mapa.goalx,mapa.goaly)
        self.binary = mapa.binarna_mapa()

        self.path = []       
        self.path_index = 0
        self.reached_goal = False
        self.path_x = [x]
        self.path_y = [y]

    # Metódy na pohyb vozidla v štyroch smeroch
    def go_forward(self):
        self.set_direction(90)
        self.step()
    
    def go_left(self):
        self.set_direction(180)
        self.step()

    def go_right(self):
        self.set_direction(0)
        self.step()

    def go_backward(self):
        self.set_direction(270)
        self.step()

    #Funkcia na hladanie cesty pomocou BFS(prehladávanie do šírky)
    def find_path(self):
        print(self.binary)
        #print(self.goal)

        # Definovanie počiatočnej a cieľovej pozície
        start = (self.x,self.y)
        goal = self.goal
        
        #pohyb = lavo,pravo,dole,hore
        smery = [(-1,0),(1,0),(0,-1),(0,1)]

        # Fronta pre BFS
        queue = deque([(start, [start])]) # Inicializacia fronty [(pozicia, [cesta])]
        visited = set([start]) # Množina navštívených uzlov

        while queue:
            (x, y), path = queue.popleft() # vyberie pvri prvok z fronty
        
            # Pripad ked je dosiahnuty ciel
            if (x,y) == goal:
                self.path = path
                print("Cesta nájdená:", path)
                return path

            #Skúška všetkých možných smerov
            for dx, dy in smery:    
                nx = int(x + dx)
                ny = int(y + dy)

                # Overenie hraníc mapy 
                if 0 <= nx < self.mapa.width and 0 <= ny < self.mapa.height:
                    # Kontrola ci neni prekazka, alebo ci uz neni dana pozicia ulozena
                    if self.binary[ny][nx] == 0 and (nx, ny) not in visited: # numpy matica ma zapis [y,x]
                        visited.add((nx, ny))
                        queue.append(((nx, ny), path + [(nx, ny)]))
        
        print("Neexistuje cesta")
        return None
    
    def follow_path(self):
        # Prípad ak nie je cesta 
        if not self.path:
            print("Neexistuje cesta")
            return
        
        for next_node in self.path[1:]:
            nx,ny = next_node

            # Vypočítanie potrebného smeru
            dx = int(nx - self.x)
            dy = int(ny - self.y)

            # Pohyb v smere 
            if dx == -1 and dy == 0:
                self.go_left()
            elif dx == 1 and dy == 0:
                self.go_right()
            elif dx == 0 and dy == 1:
                self.go_forward()
            elif dx == 0 and dy == -1:
                self.go_backward()
            else:
                print("Chyba v pohybe")
