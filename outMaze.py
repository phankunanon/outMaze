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
            self.player1_sprite = ModelSprite('images\player2.png',model=self.world.player1)

    def on_draw(self):
        arcade.start_render()
        self.player1_sprite.draw()

if __name__ == '__main__':
    window = outMazeWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()