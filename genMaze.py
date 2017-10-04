import arcade
import math
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 600
Block_Size = 16
SPRITE_SCALING = 1
Body_Size = 36
class Maze():
    def __init__(self):
        self.maze1 = arcade.SpriteList()
        set_maze = self.Set_wall
        for y in range(5,SCREEN_HEIGHT,Block_Size+15):
            x = math.floor(Block_Size*SPRITE_SCALING)
            set_maze(x,y)
        
        set_maze(48,100)
        set_maze(80,100)
        set_maze(112,100)
        set_maze(144,100)
        set_maze(144,132)
        set_maze(144,164)
        set_maze(144,196)
        set_maze(176,196)
        set_maze(208,196)
        set_maze(240,100)
        set_maze(240,196)
        set_maze(272,196)
        set_maze(272,100)
        set_maze(304,196)
        set_maze(304,164)
        set_maze(304,132)
        set_maze(304,100)
    def Set_wall(self,x,y):
        wall = arcade.Sprite("images/Block2.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = y
        self.maze1.append(wall)