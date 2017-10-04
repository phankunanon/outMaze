import arcade
from model import World
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 600
Block_Size = 32
SPRITE_SCALING = 1
class ModelSprite(arcade.Sprite):
    def __init__(self,*args,**kwargs):
        self.model = kwargs.pop('model',None)

        super().__init__(*args,**kwargs)

    def sync_with_model(self):
        if self.model:
            self.set_position(self.model.x,self.model.y)
    
    def draw(self):
        self.sync_with_model()
        super().draw()

class outMazeWindow(arcade.Window):
    def __init__(self,width,height):
            super().__init__(width,height)
            arcade.set_background_color(arcade.color.BLACK)          
            self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.player1_sprite = ModelSprite('images\Bear.png',model=self.world.player1)
            self.wall =  self.world.wall_list
            self.wall_mazepl1 = self.world.wall_mazepl1
 
    def on_draw(self):
        arcade.start_render()
        self.player1_sprite.draw()
        self.wall.draw()
        self.wall_mazepl1.draw()
    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self,key,key_modifiers):
        self.world.on_key_release(key,key_modifiers)

    def update(self, delta):
        self.world.update(delta)
        
if __name__ == '__main__':
    window = outMazeWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()