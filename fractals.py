import arcade
from shader import Shader

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Fractal Plotter"

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.time = 0
        self.scaleFactor = 0
        self.offset = [0, 0]
        self.shader = Shader()
        self.set_update_rate = 1/60
        self.pressed = [0,0,0,0]

    def on_draw(self):
        arcade.start_render()
        self.shader.draw(time=self.time, scaleFactor=self.scaleFactor, offset=self.offset)

    def on_update(self, dt):
        self.time += dt
        self.offset[1] -= 0.1 * self.pressed[0] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        self.offset[1] += 0.1 * self.pressed[2] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        self.offset[0] -= 0.1 * self.pressed[1] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        self.offset[0] += 0.1 * self.pressed[3] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)


    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
       self.shader.mouse_pos = x, y
    
    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
       self.shader.mouse_pos = x, y
       self.scaleFactor += scroll_y/10

    def on_key_press(self, key, modifiers):
        #W=119, A=97, S=115, D=100
        self.pressed = [self.pressed[0] or key==119, self.pressed[1] or key==97, self.pressed[2] or key==115, self.pressed[3] or key==100]
    
    def on_key_release(self, key, modifiers):
        if (key == 119): self.pressed[0] = 0
        if (key == 97): self.pressed[1] = 0
        if (key == 115): self.pressed[2] = 0
        if (key == 100): self.pressed[3] = 0


if __name__ == "__main__":
    Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
