import arcade.key
from random import randint
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
        self.count = 0
        self.press_up = False
        self.win = False
        self.got_warb = False
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

        for wall in self.world.wall_maze1:
            if self.hit(wall, 40):
                self.x -= self.delta_x
                self.y -= self.delta_y
        for wall in self.world.wall_maze2:
            if self.hit(wall, 40):
                self.x -= self.delta_x
                self.y -= self.delta_y
                
        for i in self.world.item1:
            if self.hit(i, 45):
                i.kill()
                self.count += 1

        for i in self.world.item2:
            if self.hit(i, 45):
                i.kill()
                self.count += 1
        warb1 = 0
        warb2 = 0
        for i in self.world.warb1:
            if self.hit(i,20) and self.count == 3 and self.press_up and (self.world.true_warb1 == warb1):
                print("Ch ")
                self.win = True
            warb1 += 1

        for i in self.world.warb2:
            if self.hit(i,20) and self.count == 3 and self.press_up and (self.world.true_warb2 == warb2) :
                print("Ch ")
                self.win = True
            warb2 += 1

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height
        self.wall_maze = arcade.SpriteList()
        self.mark = [0,0,0,0,0,0,0,0,0,0]
        #Gen_maze
        #self.wall_maze
        self.wall_maze1 = Maze().maze1
        self.wall_maze2 = Maze().maze2
        self.warb1 = Maze().warb1
        self.warb2 = Maze().warb2
        self.Item1 = Maze().item1
        self.Item2 = Maze().item2
        self.item1 = arcade.SpriteList()
        self.item2 = arcade.SpriteList()
        num1 = randint(0,2)
        num2 = randint(0,2)
        self.true_warb1 = num1
        self.true_warb2 = num2
        print(num1)
        print(num2)
        while len(self.item1)+len(self.item2)<6 :
            num = randint(0,5)
            while self.mark[num] != 0:
                num = randint(0,5)
            self.mark[num]=1
            self.item1.append(self.Item1[num])
            self.item2.append(self.Item2[num])

        self.player1 = Player(self,36*2,36*2)
        self.player2 = Player(self,SCREEN_WIDTH//2 +36*2,36*2)


    def update(self, delta):
        if not(self.player1.win) and not(self.player2.win):
            self.player1.update(delta)
            self.player2.update(delta)

    def on_key_press(self, key, key_modifiers):

        if key == arcade.key.UP: 
            self.player2.delta_y = Move_Speed
            self.player2.press_up = True
        elif key == arcade.key.DOWN:
            self.player2.delta_y = Move_Speed*-1
        elif key == arcade.key.LEFT: 
            self.player2.delta_x = Move_Speed*-1
        elif key == arcade.key.RIGHT:
            self.player2.delta_x = Move_Speed

        if key == arcade.key.W: 
            self.player1.delta_y = Move_Speed
            self.player1.press_up = True
        elif key == arcade.key.S:
            self.player1.delta_y = Move_Speed*-1
        elif key == arcade.key.D: 
            self.player1.delta_x = Move_Speed
        elif key == arcade.key.A:
            self.player1.delta_x = Move_Speed*-1

    def on_key_release(self,key,key_modifiers):
        if key == arcade.key.W or key == arcade.key.S:
            if key == arcade.key.W:
                self.player1.press_up = False
            self.player1.delta_y = 0
        elif key == arcade.key.D or key == arcade.key.A:
            self.player1.delta_x = 0

        if key == arcade.key.UP or key == arcade.key.DOWN:
            self.player2.delta_y = 0
            if key == arcade.key.UP:
                self.player2.press_up = False
        elif key == arcade.key.LEFT or key == arcade.key.RIGHT:
            self.player2.delta_x = 0
