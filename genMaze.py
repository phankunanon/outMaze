import arcade
import math
from Setup import set_up
SCREEN_WIDTH = set_up().SCREEN_WIDTH
SCREEN_HEIGHT = set_up().SCREEN_HEIGHT
Block_Size = set_up().Block_Size
SPRITE_SCALING = set_up().SPRITE_SCALING
Body_Size = set_up().Body_Size
Map_Size = set_up().Map_Size
class Maze():
    def __init__(self):
        self.maze = arcade.SpriteList()
        self.warb = arcade.SpriteList()
        set_maze = self.Set_wall
        
        map_string = (
            "#########################",
            "#.X.........X.#.........#",
            "#.............#.........#",
            "#..#..#########..#####..#",
            "#..#..#....#.X#......#..#",
            "#..#..#...w#..#......#..#",
            "#..#..#..###..#####..#..#",
            "#..#..#..X.#.........#..#",
            "#..#..#....#.........#..#",
            "#..#..###..#...#######..#",
            "#..#.......#...#.....#..#",
            "#..#.......#...#.....#..#",
            "#..#..######...#..#..#..#",
            "#.....#........#..#.....#",
            "#.....#.w......#..#.....#",
            "#..#############..###...#",
            "#..#...........#..#.....#",
            "#..#...........#..#.....#",
            "#..#..######...#..#..####",
            "#X....#....#......#.....#",
            "#.....#..w.#....X.#.....#",
            "#######..############...#",
            "#.......................#",
            "#.......................#",
            "#########################",
        )
        for x in range (0,Map_Size):
            for y in range (0,Map_Size) :
                if map_string[Map_Size-1-x][y] == ".":
                    continue
                elif map_string[Map_Size-1-x][y] == "w":
                    set_maze(y*Body_Size,x*Body_Size+17,"images/wab.jpg",0.175)
                else :
                    set_maze(y*Body_Size,x*Body_Size,"images/Block2.png",SPRITE_SCALING)

    def Set_wall(self,x,y,name_pic,scaling):
        wall = arcade.Sprite(name_pic, scaling)
        wall.center_x = x+Body_Size//2
        wall.center_y = y+Body_Size//2

        if name_pic == "images/Block2.png":
            self.maze.append(wall)
        else :
            self.warb.append(wall)

        wall2 = arcade.Sprite(name_pic, scaling)
        wall2.center_x = x+Body_Size//2 + SCREEN_WIDTH//2 - 10
        wall2.center_y = y+Body_Size//2

        if name_pic == "images/Block2.png":
            self.maze.append(wall2)
        else :
            self.warb.append(wall2)