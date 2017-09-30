import arcade
from model import World
SCREEN_WIDTH = 1400
SCREEN_HEIGHT = 700

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
            self.divide_screen = ModelSprite('images\dividescreen.png',model = self.world.divide_screen)
            self.player1_sprite = ModelSprite('images\player2.png',model=self.world.player1)

    def on_draw(self):
        arcade.start_render()
        self.player1_sprite.draw()
        self.divide_screen.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self,key,key_modifiers):
        self.world.on_key_release(key,key_modifiers)

    def update(self, delta):
        self.world.update(delta)    

if __name__ == '__main__':
    window = outMazeWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()