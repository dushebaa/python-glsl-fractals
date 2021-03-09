import arcade
from arcade.experimental.shadertoy import ShaderToy

# Do the math to figure out our screen dimensions
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "mandelbrot"

shader = open('shader.glsl', 'r').read()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.time = 0
        self.shadertoy = ShaderToy(shader)
        

    def on_draw(self):
        arcade.start_render()
        self.shadertoy.draw(time=self.time)

    def on_update(self, dt):
        # Keep track of elapsed time
        self.time += dt
        #print(1/dt)

    def on_mouse_drag(self, x, y, dx, dy, buttons, modifiers):
        self.shadertoy.mouse_pos = x, y


if __name__ == "__main__":
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()