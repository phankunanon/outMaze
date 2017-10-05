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
        set_maze = self.Set_wall
        
        map_string = (
            "############..###########",
            "#.............#.........#",
            "#.............#.........#",
            "#..#..#########..#####..#",
            "#..#..#....#..#......#..#",
            "#..#..#....#..#......#..#",
            "#..#..#..###..#####..#..#",
            "#..#..#....#.........#..#",
            "#..#..#....#.........#..#",
            "#..#..###..#...#######..#",
            "#..#.......#...#.....#..#",
            "#..#.......#...#.....#..#",
            "#..#..######...#..#..#..#",
            "#.....#........#..#.....#",
            "#.....#........#..#.....#",
            "#..#############..###...#",
            "#..#...........#..#.....#",
            "#..#...........#..#.....#",
            "#..#..######...#..#..####",
            "#.....#....#......#.....#",
            "#.....#....#......#.....#",
            "#######..############...#",
            "#.......................#",
            "#.......................#",
            "#########################",
        )
        for x in range (0,Map_Size):
            for y in range (0,Map_Size) :
                if map_string[Map_Size-1-x][y] == "#":
                    set_maze(y*Body_Size,x*Body_Size)

    def Set_wall(self,x,y):
        wall = arcade.Sprite("images/Block2.png", SPRITE_SCALING)
        wall.center_x = x+Body_Size//2
        wall.center_y = y+Body_Size//2
        self.maze.append(wall)
        wall2 = arcade.Sprite("images/Block2.png", SPRITE_SCALING)
        wall2.center_x = x+Body_Size//2 + SCREEN_WIDTH//2 - 10
        wall2.center_y = y+Body_Size//2
        self.maze.append(wall2)
        