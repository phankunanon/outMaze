import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
DIR_NOKEY = 0
DIR_OFFSET = { DIR_UP: (0,1),
               DIR_RIGHT: (1,0),
               DIR_DOWN: (0,-1),
               DIR_LEFT: (-1,0) ,
               DIR_NOKEY:(0,0)}

KEY_OFFSET = { arcade.key.UP: DIR_UP,
               arcade.key.DOWN: DIR_DOWN,
               arcade.key.LEFT: DIR_LEFT,
               arcade.key.RIGHT: DIR_RIGHT}

class Model:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y

class Player(Model):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.player1 = Player(self,width//2,height//2) # x,y = start point