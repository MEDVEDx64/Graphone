from . import base
from . import interactive

from pygame import gfxdraw, display
from utils.data import DataContainer


class Drawing(list, DataContainer):
    def __init__(self):
        super(Drawing, self).__init__()
        self.color = (255, 255, 255)

    def prefix(self):
        return 'drawing'


class ShapeLayer(base.InteractiveLayer):
    def __init__(self, app, parent=None):
        super(ShapeLayer, self).__init__(app)
        self.parent = parent


class LineShapeLayer(ShapeLayer, interactive.DraggableVertexLayer):
    def __init__(self, app, parent=None):
        super(LineShapeLayer, self).__init__(app, parent)

    def render(self):
        super(LineShapeLayer, self).render()
        screen = display.get_surface()
        color = (255, 255, 255)
        if self.parent:
            color = self.parent.color
        gfxdraw.line(screen, self.x + self.app.context.offset_x,
                     self.y + self.app.context.offset_y,
                     self.x2 + self.app.context.offset_x,
                     self.y2 + self.app.context.offset_y, color)
