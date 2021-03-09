import arcade
from arcade.experimental.shadertoy import ShaderToy

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "window"

shader = open('shader.glsl', 'r').read()


class MyGame(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.time = 0
        self.shadertoy = ShaderToy(shader)
        self.set_vsync = True

    def on_draw(self):
        arcade.start_render()
        self.shadertoy.draw(time=self.time)

    def on_update(self, dt):
        self.time += dt

    def on_mouse_drag(self, x: float, y: float, dx: float, dy: float, _buttons: int, _modifiers: int):
        self.shadertoy.mouse_pos = x, y


if __name__ == "__main__":
    MyGame(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()
