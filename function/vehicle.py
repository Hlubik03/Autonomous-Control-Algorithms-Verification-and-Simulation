import math

class vehicle():
    def __init__(self,x,y,speed,direction):
        """
        Základná trieda reprezentujúca vozidlo.
                
        x: počiatočná x-ová pozícia
        y: počiatočná y-ová pozícia
        speed: rýchlosť  
        direction: smer pohybu v stupňoch (0 = vpravo, 90 = hore)
        """
        self.x = x
        self.y = y
        self.speed = speed
        self.direction = direction
        self.path_x = [x]
        self.path_y = [y]

    def get_speed(self):
        # Vráti rýchlosť vozidla
        return self.speed
    
    def set_speed(self,new_speed: float):
        # Zmení rýchlosť vozidla
        self.speed = new_speed

    def set_direction(self,new_direction: float):
        # Zmení smer vozidla
        self.direction = new_direction % 360

    def step(self):
        # pohyb na 2d poli: [x,y] = [cos(radian), sin(radian)]
        radian = math.radians(self.direction)

        self.x += self.speed * math.cos(radian)
        self.y += self.speed * math.sin(radian)

        # zaokrúhlenie na integer
        self.x = int(round(self.x))
        self.y = int(round(self.y))

        self.path_x.append(self.x)
        self.path_y.append(self.y)

    def __repr__(self):
        # Vypis akutalnej polohy,rychlosti a smeru
        return('x {} a y {} rychlost {} smer {}'.format(self.x,self.y,self.speed,self.direction))