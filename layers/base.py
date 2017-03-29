class Layer(object):
    def __init__(self, app):
        self.app = app
        self.x = 0
        self.y = 0

    def render(self): pass


class InteractiveLayer(Layer):
    def tick(self, events): pass
