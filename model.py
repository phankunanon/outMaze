import arcade.key
from genMaze import Maze
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
SCREEN_HEIGHT = 600
Block_Size = 32
SPRITE_SCALING = 1

class Model:
    def __init__(self,world,x,y):
        self.world = world
        self.x = x
        self.y = y

    def hit(self,other,hit_size):
         return (abs(self.x - other.center_x) <= hit_size) and (abs(self.y - other.center_y) <= hit_size)

class Player(Model):
    def __init__(self,world,x,y):
        super().__init__(world,x,y)
        self.direction = DIR_NOKEY

    def update(self,delta):
        self.x += DIR_OFFSET[self.direction][0]
        self.y += DIR_OFFSET[self.direction][1]

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
        self.player1 = Player(self,90,36)
        self.wall_list = arcade.SpriteList()
        self.wall_mazepl1 = arcade.SpriteList()
        #divide wall
        for y in range(0,SCREEN_HEIGHT,Block_Size+27):
            wall = arcade.Sprite("images/Block.png", SPRITE_SCALING)
            wall.center_x = SCREEN_WIDTH//2
            wall.center_y = y
            self.wall_list.append(wall)

        #Gen_maze
        self.wall_mazepl1 = Maze().maze1

    def update(self, delta):
        self.player1.update(delta)
        for wall in self.wall_list:
            if self.player1.hit(wall, Block_Size+13):
                self.player1.x -= DIR_OFFSET[self.player1.direction][0]
                self.player1.y -= DIR_OFFSET[self.player1.direction][1]
        
        for wall in self.wall_mazepl1:
            if self.player1.hit(wall, 32):
                self.player1.x -= DIR_OFFSET[self.player1.direction][0]
                self.player1.y -= DIR_OFFSET[self.player1.direction][1]
        
    def on_key_press(self, key, key_modifiers):
        self.player1.direction = Key_OFFSET[key]
    
    def on_key_release(self,key,key_modifiers):
        self.player1.direction = DIR_NOKEY
