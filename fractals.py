import arcade
import numpy as np
import sounddevice as sd
from scipy import interpolate
from shader import Shader

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600
SCREEN_TITLE = "Fractal Plotter"

MAX_ITERS = 50

SAMPLERATE = 8000
SOUND_DURATION = 2.0

class Window(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title, resizable=True)
        self.time = 0
        self.scaleFactor = 0
        self.offset = [0, 0]
        self.shader = Shader()
        self.set_update_rate = 1/144
        self.pressed = [0]*4
        self.line = [[0]*4]

    def resetLines(self):
        self.line = [[0]*4]

    def on_draw(self):
        arcade.start_render()
        self.shader.draw(time=self.time, scaleFactor=self.scaleFactor, offset=self.offset)
        arcade.draw_line_strip(self.line, arcade.color.RED)


    def on_update(self, dt):
        self.time += dt
        self.offset[1] -= 0.1 * self.pressed[0] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        self.offset[1] += 0.1 * self.pressed[2] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        self.offset[0] -= 0.1 * self.pressed[1] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        self.offset[0] += 0.1 * self.pressed[3] / pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)


    def on_mouse_drag(self, x, y, dx, dy, _buttons, _modifiers):
       self.shader.mouse_pos = x, y

       self.on_mouse_press(x, y, 0)

    # def on_mouse_release(self, x: float, y: float, button: int, modifiers: int):
    #     self.resetLines()

    def on_mouse_scroll(self, x, y, scroll_x, scroll_y):
        self.resetLines()
        self.shader.mouse_pos = x, y
        self.scaleFactor += scroll_y/10
    

    def on_key_press(self, key, modifiers):
        self.resetLines()
        #W=119, A=97, S=115, D=100
        self.pressed = [self.pressed[0] or key==119, self.pressed[1] or key==97, self.pressed[2] or key==115, self.pressed[3] or key==100]
    
    def on_key_release(self, key, modifiers):
        if (key == 119): self.pressed[0] = 0
        if (key == 97): self.pressed[1] = 0
        if (key == 115): self.pressed[2] = 0
        if (key == 100): self.pressed[3] = 0

    def on_mouse_press(self, x: float, y: float, button: int):
        uv = [x / SCREEN_WIDTH, y/SCREEN_HEIGHT]
        theta = pow(abs(self.scaleFactor)+1, abs(self.scaleFactor)+1)
        scaledx = self.offset[0] + (3*uv[0] - 1.5) / theta
        scaledy = self.offset[1] + (2*uv[1] - 1) / theta
        
        z = 0
        n = 0
        c = complex(scaledx, scaledy)
        self.line = []
        while abs(z) <= 2 and n < MAX_ITERS:
            oldz = z
            z = z*z + c
            n += 1

            line = [0]*4
            line[0] = SCREEN_WIDTH/3 * (oldz.real * theta + 1.5) 
            line[1] = SCREEN_WIDTH/2 * (oldz.imag * theta + 1)
            # line[0], line[1] = scaledx, scaledy

            line[2] = SCREEN_WIDTH/3 * (z.real * theta + 1.5)  
            line[3] = SCREEN_WIDTH/2 * (z.imag * theta + 1)
            self.line.append(line)
            #print(line)

        
        # array = self.line
        # TODO 
        # clown -> f = interp1d(x, y, kind='cubic')
        # this shit -> https://python-sounddevice.readthedocs.io/en/0.4.2/examples.html#play-a-sound-file
        

        for i in range(len(self.line)-1):
            self.line[i][0] -= self.line[i+1]
        
        self.line.pop()

        print(self.line)
        
        waveform = np.array(self.line)


if __name__ == "__main__":
    Window(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    arcade.run()