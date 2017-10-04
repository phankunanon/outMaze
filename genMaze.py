import arcade
import math
# Not use this code
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700
Block_Size = 16
SPRITE_SCALING = 1
Body_Size = 36
class Maze():
    def __init__(self):
        self.maze1 = arcade.SpriteList()
        set_maze = self.Set_wall
        for y in range(5,SCREEN_HEIGHT,Block_Size+15):
            x = Block_Size
            set_maze(x,y)
        cnt = 0
        for x in range(Block_Size*3,SCREEN_WIDTH//2 - Block_Size,Block_Size+15):
            y = SCREEN_HEIGHT-Block_Size
            if cnt != 4 and cnt != 5 :
                set_maze(x,y)
            cnt+=1
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
        
        set_maze(336,100)
        
        set_maze(368,100)
        
        set_maze(400,100)
        set_maze(400,196)
        set_maze(400,228)
        set_maze(400,292)
        set_maze(400,260)
        set_maze(400,292)
        set_maze(400,324)
        set_maze(400,356)   
        set_maze(400,388)
        set_maze(400,420)
        set_maze(400,452)
        set_maze(400,484)
        set_maze(400,516)
        set_maze(400,548)
        set_maze(400,570)
        set_maze(400,602)
        set_maze(400,634)
        set_maze(400,666)

        set_maze(432,100)
        set_maze(432,484)

        set_maze(464,100)
        set_maze(464,484)


        set_maze(496,100)
        set_maze(496,132)
        set_maze(496,164)
        set_maze(496,196)
        set_maze(496,228)
        set_maze(496,292)
        set_maze(496,260)
        set_maze(496,292)
        set_maze(496,324)
        set_maze(496,356)
        set_maze(496,388)
        set_maze(496,484)


        set_maze(528,100)
        set_maze(528,292)
        set_maze(528,484)
        
        set_maze(560,100)
        set_maze(560,292)
        set_maze(560,484)

        set_maze(592,100)
        set_maze(592,196)
        set_maze(592,292)
        set_maze(592,388)
        set_maze(592,420)
        set_maze(592,452)
        set_maze(592,484)

        set_maze(624,196)
        
        set_maze(656,196)

    def Set_wall(self,x,y):
        wall = arcade.Sprite("images/Block2.png", SPRITE_SCALING)
        wall.center_x = x
        wall.center_y = y
        self.maze1.append(wall)