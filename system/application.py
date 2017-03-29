import layers
import pygame
import os

from utils import keyboard
from importlib.machinery import SourceFileLoader


class GraphoneApp(object):
    def __init__(self, config, initial_context):
        self.running = True
        self.clock = pygame.time.Clock()
        self.km = keyboard.KeyboardManager()

        self.config = config
        self.context = None
        self._next_ctx_name = initial_context

        # Starting pygame and creating screen
        pygame.init()
        pygame.display.set_mode(config['screen'])
        pygame.display.set_caption('Graphone')

        while self.running:
            self.clock.tick(60)
            if self._next_ctx_name:
                self._load_context(self._next_ctx_name)
                self._next_ctx_name = None
            if not self.context:
                continue

            flat = []

            def _add(lst):
                for layer in lst:
                    if isinstance(layer, layers.base.Layer):
                        flat.append(layer)
                    elif isinstance(layer, list):
                        _add(layer)

            _add(self.context.layers)

            events = pygame.event.get()

            for l in reversed(flat):
                if isinstance(l, layers.base.InteractiveLayer):
                    l.tick(events)
            for l in flat:
                l.render()
            pygame.display.flip()

        self.cleanup()

    def _load_context(self, name):
        module_name = 'contexts.' + name
        self.context = SourceFileLoader(module_name,
                                        module_name.replace('.',
                                                            os.path.sep) + '.py').load_module().provide_context(self)

    def set_context(self, name):
        self._next_ctx_name = name

    def cleanup(self):
        pass
