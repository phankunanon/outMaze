import arcade
from model import World
from Setup import set_up
SCREEN_WIDTH = set_up().SCREEN_WIDTH
SCREEN_HEIGHT = set_up().SCREEN_HEIGHT
Block_Size = set_up().Block_Size
SPRITE_SCALING = set_up().SPRITE_SCALING
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
            arcade.set_background_color(arcade.color.LIGHT_TAUPE)          
            self.world = World(SCREEN_WIDTH, SCREEN_HEIGHT)
            self.player1_sprite = ModelSprite('images\Bear.png',model=self.world.player1)
            self.player2_sprite = ModelSprite('images\pig.png',model=self.world.player2)

    def on_draw(self):
        arcade.start_render()
        self.world.wall_maze1.draw()
        self.world.warb1.draw()
        self.world.wall_maze2.draw()
        self.world.warb2.draw()
        self.world.item1.draw()
        self.world.item2.draw()
        if not(self.world.player2.win):
            self.player1_sprite.draw()
        if not(self.world.player1.win):
            self.player2_sprite.draw()

    def on_key_press(self, key, key_modifiers):
        self.world.on_key_press(key, key_modifiers)

    def on_key_release(self,key,key_modifiers):
        self.world.on_key_release(key,key_modifiers)

    def update(self, delta):
        self.world.update(delta)
        
if __name__ == '__main__':
    window = outMazeWindow(SCREEN_WIDTH,SCREEN_HEIGHT)
    arcade.run()