import arcade.key

DIR_UP = 1
DIR_RIGHT = 2
DIR_DOWN = 3
DIR_LEFT = 4
DIR_NOKEY = 0
DIR_OFFSET = { DIR_UP: (0,10),
               DIR_RIGHT: (10,0),
               DIR_DOWN: (0,-10),
               DIR_LEFT: (-10,0) ,
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
        self.direction = DIR_NOKEY

    def update(self,delta):
        self.x += DIR_OFFSET[self.direction][0]
        self.y += DIR_OFFSET[self.direction][1]

class World:
    def __init__(self,width,height):
        self.width = width
        self.height = height

        self.player1 = Player(self,width//2,height//2)

    def update(self, delta):
        self.player1.update(delta)

    def on_key_press(self, key, key_modifiers):
        self.player1.direction = KEY_OFFSET[key]
    
    def on_key_release(self,key,key_modifiers):
        self.player1.direction = DIR_NOKEY