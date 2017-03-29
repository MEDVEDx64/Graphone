from . import base

from pygame.locals import *
from pygame import gfxdraw, display


class DraggableVertexLayer(base.InteractiveLayer):
    def __init__(self, app):
        super(DraggableVertexLayer, self).__init__(app)
        self.x2 = 0
        self.y2 = 0

        self.vertex_range = 5

        self.hover = False
        self.hover2 = False
        self.moving = False
        self.dragging = False
        self.dragging2 = False

        self.force_moving = False

    # Does the mouse cursor hovers vertex?
    def cross(self, pos, x, y):
        if pos[0] >= (x + self.app.context.offset_x - self.vertex_range)    \
        and pos[0] <= (x + self.app.context.offset_x + self.vertex_range)   \
        and pos[1] >= (y + self.app.context.offset_y - self.vertex_range)   \
        and pos[1] <= (y + self.app.context.offset_y + self.vertex_range):
            return True
        return False

    def tick(self, events):
        pos = None
        for ev in events:
            if ev.type == MOUSEMOTION or ev.type == MOUSEBUTTONDOWN:
                pos = ev.pos
                self.hover = self.cross(pos, self.x, self.y)
                self.hover2 = self.cross(pos, self.x2, self.y2)
            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1:
                    self.dragging = self.hover
                    if not self.hover:
                        self.dragging2 = self.hover2
                elif ev.button == 3:
                    self.dragging = self.hover
                    self.dragging2 = self.hover2
                    self.moving = self.hover or self.hover2 or self.force_moving
            elif ev.type == MOUSEBUTTONUP:
                self.moving = False
                self.dragging = False
                self.dragging2 = False

        # Moving vertex or entire line
        if pos:
            if self.moving:
                vec_x = 0
                vec_y = 0

                if self.dragging:
                    vec_x = pos[0] - self.app.context.offset_x - self.x
                    vec_y = pos[1] - self.app.context.offset_y - self.y

                elif self.dragging2:
                    vec_x = pos[0] - self.app.context.offset_x - self.x2
                    vec_y = pos[1] - self.app.context.offset_y - self.y2

                self.x += vec_x
                self.y += vec_y
                self.x2 += vec_x
                self.y2 += vec_y

            else:
                if self.dragging:
                    self.x += pos[0] - self.app.context.offset_x - self.x
                    self.y += pos[1] - self.app.context.offset_y - self.y

                elif self.dragging2:
                    self.x2 += pos[0] - self.app.context.offset_x - self.x2
                    self.y2 += pos[1] - self.app.context.offset_y - self.y2

    def render(self):
        screen = display.get_surface()
        # Drawing circles
        if self.hover or self.hover2:
            color = (96, 128, 255, 128)
            if self.dragging or self.dragging2:
                color = (255, 128, 96, 128)
            if self.hover:
                gfxdraw.circle(screen,
                               self.x + self.app.context.offset_x,
                               self.y + self.app.context.offset_y,
                               self.vertex_range, color)
            if self.hover2:
                gfxdraw.circle(screen,
                               self.x2 + self.app.context.offset_x,
                               self.y2 + self.app.context.offset_y,
                               self.vertex_range, color)


class DraggableRectangleLayer(DraggableVertexLayer):
    # Can be overridden to handle mouse clicks
    def click(self): pass

    def rect_cross(self, pos, x, y, x2, y2):
        if pos[0] >= (x + self.app.context.offset_x)    \
        and pos[0] <= (x2 + self.app.context.offset_x)  \
        and pos[1] >= (y + self.app.context.offset_y)   \
        and pos[1] <= (y2 + self.app.context.offset_y):
            return True
        return False

    def tick(self, events):
        for ev in events:
            cross = False
            if ev.type == MOUSEMOTION or ev.type == MOUSEBUTTONDOWN:
                cross = self.rect_cross(
                    ev.pos,
                    self.x, self.y,
                    self.x2, self.y2)

            if ev.type == MOUSEBUTTONDOWN:
                if ev.button == 1 and cross:
                    self.click()
                if ev.button == 3:
                    self.force_moving = cross

            if ev.type == MOUSEBUTTONUP:
                self.force_moving = False

        super(DraggableRectangleLayer, self).tick(events)
