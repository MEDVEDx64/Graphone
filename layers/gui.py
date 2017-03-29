from . import interactive

from pygame import gfxdraw, display


class WindowLayer(interactive.DraggableRectangleLayer):
    def __init__(self, app):
        super(WindowLayer, self).__init__(app)
        self.bgcolor = (160, 200, 32, 128)
        self.fgcolor = (224, 224, 255)

    def render(self):
        super(WindowLayer, self).render()
        screen = display.get_surface()
        gfxdraw.box(screen, (self.x + 1, self.y + 1, self.x2 - 1, self.y2 - 1), self.bgcolor)
        gfxdraw.rectangle(screen, (self.x, self.y, self.x2, self.y2), self.fgcolor)


class FpsCounterLayer(interactive.DraggableRectangleLayer):
    def __init__(self, app):
        super(FpsCounterLayer, self).__init__(app)
        self.x = 700

    def render(self):
        fps = self.app.font.render('FPS: ' + str(int(self.app.clock.get_fps())), 1, (255, 255, 0))
        display.get_surface().blit(fps, (self.x, self.y))
