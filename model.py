import arcade.key
from genMaze import Maze
from Setup import set_up
SCREEN_WIDTH = set_up().SCREEN_WIDTH
SCREEN_HEIGHT = set_up().SCREEN_HEIGHT
Block_Size = set_up().Block_Size
SPRITE_SCALING = set_up().SPRITE_SCALING
Move_Speed = set_up().Move_Speed
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
        self.player2 = Player(self,SCREEN_WIDTH//2 +36*2,36*2)
        self.wall_maze = arcade.SpriteList()

        #Gen_maze
        self.wall_maze = Maze().maze
        self.warb = Maze().warb

    def update(self, delta):
        self.player1.update(delta)
        self.player2.update(delta)

        for wall in self.wall_maze:
            if self.player1.hit(wall, 32):
                self.player1.x -= self.player1.delta_x
                self.player1.y -= self.player1.delta_y
                
            if self.player2.hit(wall, 32):
                self.player2.x -= self.player2.delta_x
                self.player2.y -= self.player2.delta_y
        
    def on_key_press(self, key, key_modifiers):
        if key == arcade.key.UP: 
            self.player2.delta_y = Move_Speed
        elif key == arcade.key.DOWN:
            self.player2.delta_y = Move_Speed*-1
        elif key == arcade.key.LEFT: 
            self.player2.delta_x = Move_Speed*-1
        elif key == arcade.key.RIGHT:
            self.player2.delta_x = Move_Speed

        if key == arcade.key.W: 
            self.player1.delta_y = Move_Speed
        elif key == arcade.key.S:
            self.player1.delta_y = Move_Speed*-1
        elif key == arcade.key.D: 
            self.player1.delta_x = Move_Speed
        elif key == arcade.key.A:
            self.player1.delta_x = Move_Speed*-1
        
    def on_key_release(self,key,key_modifiers):
        
        if key == arcade.key.W or key == arcade.key.S:
            self.player1.delta_y = 0
        elif key == arcade.key.D or key == arcade.key.A:
            self.player1.delta_x = 0

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player2.delta_y = 0
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player2.delta_x = 0
