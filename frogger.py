import pygame
import froggerlib

class Frogger:

    def __init__( self, width, height ):
        self.mWidth = width
        self.mHeight = height
        self._lane_size= 60 #changed size to 60
        self._game_over = False

        self.mDSUTan = ( 229, 217, 189 )
        
        self._lanes = []
        
        w = 0.8*self._lane_size
        h = 0.8*self._lane_size
        x = self.mWidth/2 - w/2
        y = self._lane_size * 10.5 - h/2
        dx = x
        dy = y
        s = self._lane_size/2.0
        hg = self._lane_size
        vg = self._lane_size
        self._frog = froggerlib.Frog(x,y,w,h,dx,dy,s,hg,vg)
        self._frog_color = (15,255,35)
        
        #home
        self._homes = []
        x = 0
        h = self._lane_size
        y = 0
        w = self._lane_size
        self._home_color = (200,0,100)
        home = froggerlib.Home(x,y,w,h)
        self._homes.append((home, self._home_color))
        
        
        x = self.mWidth / 2 - self._lane_size / 2
        h = self._lane_size
        y = 0
        w = self._lane_size
        self._home_color = (200,0,100)
        home = froggerlib.Home(x,y,w,h)
        self._homes.append((home, self._home_color))
        
        
        x = self.mWidth - self._lane_size
        h = self._lane_size
        y = 0
        w = self._lane_size
        self._home_color = (200,0,100)
        home = froggerlib.Home(x,y,w,h)
        self._homes.append((home, self._home_color))
        
        
        #grass
        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 5 * self._lane_size
        self._grass_color = (0,100,0)
        self._grass1 = froggerlib.Grass(x, y, w, h)
        
        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 10 * self._lane_size
        self._grass2 = froggerlib.Grass(x, y, w, h)
        
        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 0
        self._grass3 = froggerlib.Grass(x, y, w, h)
        
        # lanes
        
        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 9 * self._lane_size
        self._road_color = (0,0,0)
        road = froggerlib.Road(x, y, w, h)
        self._lanes.append((road, self._road_color))
        
        x = 1 * self.mWidth / 6
        h = 0.8 * self._lane_size
        y = self._lane_size * 9.5  - h/2
        w = 1.6*self._lane_size
        s = self._lane_size/7
        dx = self.mWidth + 5
        dy = y
        self._car_color = (255,0,0)
        car = froggerlib.Car(x,y,w,h,dx,dy,s)
        self._lanes.append((car, self._car_color))

        x = 1 * self.mWidth / 2
        car = froggerlib.Car(x,y,w,h,dx,dy,s)
        self._lanes.append((car, self._car_color))
        
        x = 5 * self.mWidth / 6
        car = froggerlib.Car(x,y,w,h,dx,dy,s)
        self._lanes.append((car, self._car_color))

        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 8 * self._lane_size
        self._road_color = (0,0,0)
        road = froggerlib.Road(x, y, w, h)
        self._lanes.append((road, self._road_color))
        
        x = 1 * self.mWidth / 6
        h = 0.8 * self._lane_size
        y = self._lane_size * 8.5  - h/2
        w = 1.5*self._lane_size
        s = self._lane_size/12
        dx = -w
        dy = y
        self._dozer_color = (0,100,200)
        dozer = froggerlib.Dozer(x,y,w,h,dx,dy,s)
        self._lanes.append((dozer, self._dozer_color))

        
        x = 3 * self.mWidth / 4
        dozer = froggerlib.Dozer(x,y,w,h,dx,dy,s)
        self._lanes.append((dozer, self._dozer_color))
        
        
        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 7 * self._lane_size
        self._road_color = (0,0,0)
        road = froggerlib.Road(x, y, w, h)
        self._lanes.append((road, self._road_color))
        
        x = 1 * self.mWidth / 6
        h = 0.8 * self._lane_size
        y = self._lane_size * 7.5  - h/2
        w = 1.2*self._lane_size
        mins = self._lane_size/10
        maxs = self._lane_size/5
        dx = self.mWidth + 5
        dy = y
        self._race_car_color = (255,255,0)
        raceCar = froggerlib.RaceCar(x,y,w,h,dx,dy,mins,maxs)
        self._lanes.append((raceCar, self._race_car_color))

        
        x = 3 * self.mWidth / 2
        raceCar = froggerlib.RaceCar(x,y,w,h,dx,dy,mins,maxs)
        self._lanes.append((raceCar, self._race_car_color))
        
        w = self.mWidth
        h = self._lane_size
        x = 0
        y = 6 * self._lane_size
        self._road_color = (0,0,0)
        road = froggerlib.Road(x, y, w, h)
        self._lanes.append((road, self._road_color))
        
        x = 1 * self.mWidth / 6
        h = 0.8 * self._lane_size
        y = self._lane_size * 6.5  - h/2
        w = 2*self._lane_size
        s = self._lane_size/8
        dx = -w
        dy = y
        self._truck_color = (200,200,200)
        truck = froggerlib.Truck(x,y,w,h,dx,dy,s)
        self._lanes.append((truck, self._truck_color))
        
        #water
        x = 0
        y = 4 * self._lane_size
        w = self.mWidth
        h = self._lane_size
        water = froggerlib.Water(x,y,w,h)
        self._water_color = (0, 50, 100)
        self._lanes.append((water, self._water_color))
        
        
        
        y = 3 * self._lane_size
        water = froggerlib.Water(x,y,w,h)
        self._lanes.append((water, self._water_color))
    
        y = 2 * self._lane_size
        water = froggerlib.Water(x,y,w,h)
        self._lanes.append((water, self._water_color))
        
        y = 1 * self._lane_size
        water = froggerlib.Water(x,y,w,h)
        self._lanes.append((water, self._water_color))
        
        x = 1 * self.mWidth / 6
        h = 0.8 * self._lane_size
        y = self._lane_size * 4.5  - h/2
        w = 2*self._lane_size
        s = self._lane_size/8
        dx = self.mWidth
        dy = y
        self._log_color = (210,105,30)
        log = froggerlib.Log(x,y,w,h,dx,dy,s)
        self._lanes.append((log, self._log_color))
        
        x = 1 * self.mWidth / 2
        dx = self.mWidth
        dy = y
        log = froggerlib.Log(x,y,w,h,dx,dy,s)
        self._lanes.append((log, self._log_color))
        
        x = 1 * self.mWidth
        dx = self.mWidth
        dy = y
        log = froggerlib.Log(x,y,w,h,dx,dy,s)
        self._lanes.append((log, self._log_color))
        
        x = 1 * self.mWidth -50
        h = 0.8 * self._lane_size
        y = self._lane_size * 3.5  - h/2
        w = 0.8 * self._lane_size
        s = self._lane_size/14
        dx = -x
        dy = y
        self._turtle_color = (0,200,0)
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth + 50
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth + 150
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth + 250
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth + 350
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth / 6
        h = 0.8 * self._lane_size
        y = self._lane_size * 2.5  - h/2
        w = 2*self._lane_size
        s = self._lane_size/6
        dx = -x
        dy = y
        log = froggerlib.Log(x,y,w,h,dx,dy,s)
        self._lanes.append((log, self._log_color))
        
        x = 1 * self.mWidth
        log = froggerlib.Log(x,y,w,h,dx,dy,s)
        self._lanes.append((log, self._log_color))
        
        x = 1 * self.mWidth -50
        h = 0.8 * self._lane_size
        y = self._lane_size * 1.5  - h/2
        w = 0.8 * self._lane_size
        s = self._lane_size/10
        dx = self.mWidth
        dy = y
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth - 200
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        x = 1 * self.mWidth - 350
        turtle = froggerlib.Turtle(x,y,w,h,dx,dy,s)
        self._lanes.append((turtle, self._turtle_color))
        
        
        return

    def actOnPressA( self ):
        return
    
    def actOnHoldA( self ):
        return
    
    def actOnHoldUP( self ):
        
        return
    
    def actOnLeftClick( self, x, y ):
        return
    
    def actOnPressUP( self ):
        self._frog.up()
        return
    def actOnPressDOWN( self ):
        self._frog.down()
        return
    def actOnPressLEFT( self ):
        self._frog.left()
        return
    def actOnPressRIGHT( self ):
        self._frog.right()
        return
    
    def evolve( self, dt ):
        if self._game_over:
            return
        self._frog.move()
        if self._frog.outOfBounds(self.mWidth, self.mHeight):
            self._game_over = True
            
        for item_tuple in self._lanes:
            item, color = item_tuple
            if isinstance(item, froggerlib.Movable):
                item.move()
                if item.atDesiredLocation():
                    if item.getDesiredX() > 0:
                        x = - item.getWidth()
                    else:
                        x = self.mWidth
                    item.setX(x)
            if item.hits(self._frog):
                self._game_over = True
            item.supports(self._frog)
        for home_tuple in self._homes:
            home, color = home_tuple
            if home.hits(self._frog):
                print("winner")
                self._game_over = True
        if self._grass3.hits(self._frog):
            self._game_over = True
            
        

    # draws the current state of the system
    def draw( self, surface ):
        
        # rectangle to fill the background
        rect = pygame.Rect( int ( 0 ), int ( 0 ), int ( self.mWidth ), int ( self.mHeight ) )
        pygame.draw.rect( surface, self.mDSUTan, rect, 0 )
        
        rect = pygame.Rect(int(self._grass1.getX()),int(self._grass1.getY()),int(self._grass1.getWidth()),int(self._grass1.getHeight()))
        pygame.draw.rect(surface, self._grass_color, rect, 0)
        
        rect = pygame.Rect(int(self._grass2.getX()),int(self._grass2.getY()),int(self._grass2.getWidth()),int(self._grass2.getHeight()))
        pygame.draw.rect(surface, self._grass_color, rect, 0)
        
        rect = pygame.Rect(int(self._grass3.getX()),int(self._grass3.getY()),int(self._grass3.getWidth()),int(self._grass3.getHeight()))
        pygame.draw.rect(surface, self._grass_color, rect, 0)
        
        for home_tuple in self._homes:
            home, color = home_tuple
            rect = pygame.Rect(int(home.getX()),int(home.getY()),int(home.getWidth()),int(home.getHeight()))
            pygame.draw.rect(surface, color, rect, 0)
        
        
        
        for item_tuple in self._lanes:
            item, color = item_tuple
            rect = pygame.Rect(int(item.getX()),int(item.getY()),int(item.getWidth()),int(item.getHeight()))
            pygame.draw.rect(surface, color, rect, 0)

        #rect = pygame.Rect(int(self._car1.getX()),int(self._car1.getY()),int(self._car1.getWidth()),int(self._car1.getHeight()))
        #pygame.draw.rect(surface, self._car_color, rect, 0)

        #rect = pygame.Rect(int(self._car2.getX()),int(self._car2.getY()),int(self._car2.getWidth()),int(self._car2.getHeight()))
        #pygame.draw.rect(surface, self._car_color, rect, 0)

        
        rect = pygame.Rect(int(self._frog.getX()),int(self._frog.getY()),int(self._frog.getWidth()),int(self._frog.getHeight()))
        pygame.draw.rect(surface, self._frog_color, rect, 0)

       
        return
