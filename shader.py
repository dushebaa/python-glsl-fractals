from arcade import get_window
from arcade.gl import geometry

class Shader:
    def __init__(self):
        self.window = get_window()
        if not self.window:
            raise RuntimeError("No window found")

        self.ctx = self.window.ctx
        self.mouse_pos = 0, 0
        self.scaleFactor = 1
        self.quad = geometry.quad_2d_fs()

        vertex   = open('vertex_shader.glsl', 'r').read()
        fragment = open('fragment_shader.glsl', 'r').read()

        self.program = self.ctx.program(
            vertex_shader=vertex,
            fragment_shader=fragment
        )
        

    def draw(self, offset = [], scaleFactor=0.1, time: float = 0, target=None):
        try:
            self.program['offsetXY'] = offset[0], offset[1]
        except KeyError:
            pass
        try:
            self.program['scaleFactor'] = scaleFactor
        except KeyError:
            pass
        try:
            self.program['iTime'] = time
        except KeyError:
            pass
        try:
            self.program['iMouse'] = self.mouse_pos[0], -self.mouse_pos[1]
        except KeyError:
            pass
        try:
            if self.window is not None:
                self.program['iResolution'] = self.window.get_framebuffer_size()
        except KeyError:
            pass

        self.quad.render(self.program)
