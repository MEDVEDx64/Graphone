from layers import decorative, technical, drawing, gui


class TestContext(object):
    def __init__(self, app):
        self.offset_x = 0
        self.offset_y = 0

        self.background = [
            decorative.GridLayer(app, 16, (16, 32, 64), (0, 16, 48)),
            decorative.GridLayer(app, 64, (48, 64, 96))
        ]
        self.shapes = [
            # debug
            drawing.Drawing()
        ]
        self.gui = [
            gui.FpsCounterLayer(app)
        ]
        self.foreground = []

        self.layers = [
            self.background,
            self.shapes,
            self.gui,
            self.foreground,

            technical.TTFInitLayer(app),
            technical.QuitHandlerLayer(app),
            technical.SimpleArrowKeysHandlerLayer(app)
        ]

        # debug
        shape1 = drawing.LineShapeLayer(app, self.shapes[0])
        shape1.x = 10
        shape1.y = 10
        shape1.x2 = 30
        shape1.y2 = 30

        shape2 = drawing.LineShapeLayer(app, self.shapes[0])
        shape2.x = 30
        shape2.y = 30
        shape2.x2 = 50
        shape2.y2 = 10

        self.shapes[0].append(shape1)
        self.shapes[0].append(shape2)


def provide_context(app):
    return TestContext(app)
