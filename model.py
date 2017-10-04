import arcade.key
from genMaze2 import Maze
DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
DIR_NOKEY = 0
DIR_OFFSET = { DIR_UP: (0,5),
               DIR_RIGHT: (5,0),
               DIR_DOWN: (0,-5),
               DIR_LEFT: (-5,0) ,
               DIR_NOKEY:(0,0)}

Key_OFFSET = { arcade.key.UP: DIR_UP,
               arcade.key.DOWN: DIR_DOWN,
               arcade.key.LEFT: DIR_LEFT,
               arcade.key.RIGHT: DIR_RIGHT}

SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 1000
Block_Size = 64
SPRITE_SCALING = 1

class Model:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y
        self.delta_x = 0
        self.delta_y = 0

    def hit(self,other,hit_size):
         return (abs(self.x - other.center_x) <= hit_size) and (abs(self.y - other.center_y) <= hit_size)

class Player(Model):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)
        self.direction = DIR_NOKEY

    def update(self,delta):
        self.x += self.delta_x
        self.y += self.delta_y

        #Check border
        if self.x > self.world.width:
            self.x = self.world.width
        elif self.x < 0:
            self.x = 0
        if self.y > self.world.height:
            self.y = self.world.height
        elif self.y < 0:
            self.y = 0

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.player1 = Player(self,36*2,36*2)
        #self.wall_list = arcade.SpriteList()
        self.wall_mazepl1 = arcade.SpriteList()
        #divide wall
        '''for y in range(Block_Size//2,SCREEN_HEIGHT,Block_Size):
            wall = arcade.Sprite("images/Block.png", SPRITE_SCALING)
            wall.center_x = SCREEN_WIDTH//2+1
            wall.center_y = y
            self.wall_list.append(wall)
'''
        #Gen_maze
        self.wall_mazepl1 = Maze().maze1

    def update(self, delta):
        self.player1.update(delta)
        '''for wall in self.wall_list:
            if self.player1.hit(wall, Block_Size):
                self.player1.x -= DIR_OFFSET[self.player1.direction][0]
                self.player1.y -= DIR_OFFSET[self.player1.direction][1]
        '''
        for wall in self.wall_mazepl1:
            if self.player1.hit(wall, 32):
                self.player1.x -= DIR_OFFSET[self.player1.direction][0]
                self.player1.y -= DIR_OFFSET[self.player1.direction][1]
        
    def on_key_press(self, key, key_modifiers):
        self.player1.direction = Key_OFFSET[key]
    
    def on_key_release(self,key,key_modifiers):
        self.player1.direction = DIR_NOKEY
