import pygame

from . import base
from pygame import gfxdraw


class GridLayer(base.Layer):
    def __init__(self, app, size=32, fg=(128, 128, 128), bg=None):
        super(GridLayer, self).__init__(app)
        self.size = size
        self.fg = fg
        self.bg = bg

    def render(self):
        scr = pygame.display.get_surface()
        res = self.app.config['screen']

        if self.bg:
            gfxdraw.box(scr, ((0, 0), res), self.bg)

        x = (self.x + self.app.context.offset_x) % self.size
        y = (self.y + self.app.context.offset_y) % self.size

        while x < res[0]:
            gfxdraw.vline(scr, x, 0, res[1], self.fg)
            x += self.size
        while y < res[1]:
            gfxdraw.hline(scr, 0, res[0], y, self.fg)
            y += self.size
