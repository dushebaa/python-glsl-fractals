import arcade
from shader import Shader

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Fractal Plotter"

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.time = 0
        self.shader = Shader()
        self.set_update_rate = 1/60;

    def on_draw(self):
        arcade.start_render()
        self.shader.draw(time=self.time)

    def on_update(self, dt):
        self.time += dt

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, _buttons: int, _modifiers: int):
       self.shader.mouse_pos = x, y
    

if __name__ == "__main__":
    Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
